# 通信领域名词

## 手机相关

### MCC
Mobile Country Code

移动国家码

MCC的资源由国际电联（ITU）统一分配和管理，唯一识别移动用户所属的国家，共3位，中国为460;

常见MCC列表：http://www.gpsspg.com/bs/mcc.htm

### MNC
Mobile Network Code

移动设备网络代码

**移动设备网络代码**（英语：Mobile Network Code，MNC）是与**移动设备国家代码**（Mobile Country Code，MCC）（也称为“MCC / MNC”）相结合，以用来表示唯一一个的移动设备的网络运营商。

中华人民共和国 - CN

|  MCC  |  MNC  |   品牌   |  运营商  |  状态  |
|  ---  |  ---  |   ----   |  ------  |  ----  |
|  460  |  00   | 中国移动 | 中国移动 |营运中  |
|  460  |  01   | 中国联通 | 中国联通 |营运中  |
|  460  |  02   | 中国移动 | 中国移动 |营运中  |
|  460  |  03   | 中国电信 | 中国电信 |营运中  |
|  460  |  05   | 中国电信 | 中国电信 |营运中  |
|  460  |  06   | 中国联通 | 中国联通 |营运中  |
|  460  |  07   | 中国移动 | 中国移动 |营运中  |
|  460  |  11   | 中国电信 | 中国电信 |营运中  |
|  460  |  20   | 中国铁通 | 中国铁通 |营运中  |

### IMSI
International Mobile Subscribe Identity

国际移动用户识别码

IMSI = MCC + MNC + MSIN (共15位)

### IMEI
Internation Mobile Equipment Identity

国际移动设备识别码

## 基站相关

### LAC
Location Area Code

位置区域码

### CID
Cell Identity

基站编号，基站小区号。CID是个16位的数据（范围是0到65535）

### PCI
Physical Cell Identifier

物理小区标识。LTE中终端以此区分不同小区的无线信号。

## 信号相关

### RSRP
Reference Signal Receiving Power

参考信号接收功率

### RSRQ
Reference Signal Receiving Quality

参考信号接收质量

### SINR
Signal to Interference plus Noise Ratio

信号与干扰加噪声比。是指接收到的有用信号的强度与接收到的干扰信号（噪声和干扰）的强度的比值；可以简单的理解为“信噪比”。

### RSSI
Received Signal Strength Indication

接收的信号强度指示

### CQI
Channel Quality Indicator

信道质量指示。

CQI是信道质量的信息指示，代表当前信道质量的好坏，和信道的信噪比大小相对应，取值范围0～31。CQI取值为0时，信道质量最差；CQI取值为31的时候，信道质量最好。


