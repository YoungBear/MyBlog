# IP 架构韧性

## 概述

IP 架构韧性（IP Network Resilience）是指 IP 网络在面对链路故障、设备故障、流量突变等异常情况时，保持业务连续性和服务质量的能力。韧性设计的核心目标是最小化故障对业务的影响，包括故障检测、快速收敛、流量切换和自动恢复。

---

## 一、网络冗余设计

### 1.1 链路冗余

通过多条物理链路连接关键节点，避免单点故障。

- **双归接入（Dual-Homing）**：一台设备同时连接到两台上游设备，一台故障时切换到另一台
- **多归接入（Multi-Homing）**：一台设备连接到多台上游设备，提供更高可用性
- **链路聚合（LAG/LACP）**：将多条物理链路绑定为一条逻辑链路，提升带宽与可用性

### 1.2 设备冗余

- **主备模式（Active-Standby）**：备用设备在正常情况下不承载流量，主设备故障后接管
- **双活模式（Active-Active）**：多台设备同时承载流量，单台故障时其余设备分担其负载
- **N+1 冗余**：N 台设备承载业务，1 台作为冷备/热备

### 1.3 拓扑冗余

| 拓扑类型 | 特点 | 适用场景 |
|---------|------|---------|
| 双平面（Dual-Plane） | 两条独立的物理/逻辑路径 | 数据中心互联 |
| 环形拓扑（Ring） | 任一单点故障不影响全网的连通性 | 城域网、承载网 |
| Full-Mesh 全网状 | 任意两节点间均有直连链路 | 核心骨干网 |
| Clos/Fat-Tree | 多级交换结构，路径丰富 | 数据中心网络 |

---

## 二、路由快速收敛

路由收敛（Convergence）是指网络拓扑变化后，所有路由器更新路由表达到一致状态的过程。收敛时间直接影响业务中断时长。

### 2.1 故障检测加速

- **BFD（Bidirectional Forwarding Detection）**：毫秒级双向转发检测，支持 50ms~300ms 检测周期，快速发现链路/节点故障，触发路由协议重新计算
- **链路层检测**：利用光模块 LOS（Loss of Signal）、以太网 Link Down 等硬件信号，故障感知在毫秒级
- **CARP（Carrier-grade Alarm Report Protocol）**：利用底层传输网告警触发上层路由收敛

### 2.2 IGP 快速收敛

- **IGP 快速 Hello**：OSPF/IS-IS 缩短 Hello 间隔至 1s 甚至子秒级，加快邻居故障检测
- **LFA（Loop-Free Alternate）**：预先计算无环备份路径，主路径故障时直接切换到备份路径，无需等待 SPF 重算
- **Remote LFA（rLFA）**：扩展 LFA 至非直连节点，通过隧道将流量引导至备份路径
- **TI-LFA（Topology Independent LFA）**：不依赖拓扑的无环备份，SR（Segment Routing）场景下的主流方案

### 2.3 BGP 快速收敛

- **BGP PIC（Prefix Independent Convergence）**：核心思想是将控制面收敛与转发面解耦。BGP 收敛时先更新转发面（快速切换至备份路径），控制面后续完成路由计算。切换时间可达亚秒级
- **BGP Graceful Restart**：控制面重启时保留转发面状态，数据转发不中断
- **BGP Add-Path**：同时通告多条路径，一条故障时可快速切换
- **BFD for BGP**：用 BFD 替代 BGP Keepalive（默认 60s），将邻居故障检测缩短到毫秒级

### 2.4 收敛时间参考

| 机制 | 典型收敛时间 |
|------|------------|
| BGP Keepalive + Hold Timer | 分钟级 |
| IGP 默认计时器（10s Hello / 40s Dead） | 数十秒 |
| IGP 快速 Hello（1s / 3s） | 数秒 |
| BFD（100ms x 3） | 约 300ms |
| BGP PIC | 亚秒级 |
| 硬件链路检测（LOS/Link Down） | 毫秒级 |

---

## 三、流量工程与负载均衡

### 3.1 等价多路径（ECMP）

Equal-Cost Multi-Path：当存在多条等价路径时，将流量均匀（或按 hash）分发到各路径上。

- **流级别负载分担**：基于五元组（src IP、dst IP、src Port、dst Port、Protocol）hash，同一条流的数据包走相同路径，避免乱序
- **限制**：当某条路径故障，所有 hash 重新分布，可能造成已有 TCP 连接中断

### 3.2 非等价多路径（UCMP）

Unequal-Cost Multi-Path：允许在带宽不同的路径上按比例分担流量。

### 3.3 隧道技术

- **MPLS TE**：通过 RSVP-TE 显式指定路径和预留带宽，实现精确的流量控制与路径保护
- **SR-TE（Segment Routing Traffic Engineering）**：基于源路由的流量工程，通过 Segment List 控制转发路径，无状态、扩展性好
- **SR Policy**：在 SR-TE 基础上抽象出业务策略，支持多条候选路径及优先级

### 3.4 一致性 Hash

- 路径变化时，仅影响与变化路径相关的流量，其余流量不受影响（minimize re-hash）
- 常见于 L4/L7 负载均衡器

---

## 四、高可用架构

### 4.1 网关冗余

- **VRRP（Virtual Router Redundancy Protocol）**：多台路由器共享一个虚拟 IP，主路由器故障时备路由器接管
- **HSRP（Hot Standby Router Protocol）**：Cisco 私有协议，功能类似 VRRP
- **GLBP（Gateway Load Balancing Protocol）**：Cisco 私有，在冗余的同时提供负载分担

### 4.2 Anycast

多台设备使用相同 IP 地址，通过路由协议将用户请求引导至最近的/最优的节点。

- 单节点故障时，路由自动收敛，流量切换到其他节点
- 广泛用于 DNS 根服务器（如 8.8.8.8）、CDN
- 要求服务是无状态的，或通过后端同步保证状态一致

### 4.3 异地多活 / 地理冗余

- **Active-Active 多 DC**：多个数据中心同时提供服务，DNS 或 BGP 按地域/优先级引导流量
- **Active-Standby DC**：主数据中心承载全量业务，灾备中心在主中心故障后接管
- **GSLB（Global Server Load Balancing）**：在 DNS 层面按健康状态、地理位置、负载等策略分发流量

---

## 五、故障隔离与容错

### 5.1 故障域隔离

- **控制面与转发面分离**：控制面故障不影响已建立会话的转发（如 SDN 控制器与交换机）
- **Pod/Cluster 隔离**：将网络划分为若干故障域，单域故障不影响其他域

### 5.2 限流与过载保护

- **CAR（Committed Access Rate）**：接口级别的流量限速，防止突发流量冲击
- **Control Plane Policing（CoPP）**：专门限制送往 CPU 的控制面流量（BGP/OSPF/ARP 等），防止 CPU 过载导致协议震荡
- **Priority Queuing**：优先保障关键业务流量（如 VoIP、信令）的转发

### 5.3 熔断与降级

- 检测到下游服务异常时，主动停止调用（熔断），或返回缓存/兜底数据（降级）
- 防止级联故障传播

---

## 六、韧性度量指标

| 指标 | 含义 | 目标值示例 |
|------|------|-----------|
| **MTBF**（Mean Time Between Failures） | 平均故障间隔时间 | 越高越好 |
| **MTTR**（Mean Time To Repair） | 平均修复时间 | 越低越好 |
| **可用性（Availability）** | MTBF / (MTBF + MTTR) | 99.999%（5个9） |
| **收敛时间** | 从故障发生到流量恢复的时间 | < 50ms（运营商级） |
| **丢包率** | 故障期间的报文丢失 | < 1s 内丢包率 |

---

## 七、韧性设计原则

1. **消除单点故障（SPOF）**：关键链路、设备、电源、控制卡都应有冗余备份
2. **故障检测要快**：硬件检测 > BFD > 快速 Hello > 默认计时器
3. **切换要快且有备份路径**：预先计算备份路径（LFA/PIC），切换时不依赖实时计算
4. **隔离故障域**：控制面与转发面解耦，单一故障不影响全局
5. **可测试、可验证**：通过 Chaos Engineering（混沌工程）定期演练故障场景，验证韧性机制的有效性
6. **渐进式降级**：无法完全避免故障时，优先保障核心业务，非核心业务降级处理
