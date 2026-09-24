# 部署设置

本站由 `.github/workflows/deploy.yml` 双部署：GitHub Pages（`/MyBlog/`）+ 自建服务器（`/`）。
以下配置均为一次性操作，请勿遗漏（尤其第 2 步，未设置时首次 push 的 deploy-pages 会失败）。

## 1. 仓库 Actions secrets（Settings → Secrets and variables → Actions）

| Secret | 说明 |
| --- | --- |
| `SSH_HOST` | 服务器公网 IP 或域名 |
| `SSH_USER` | SSH 登录用户 |
| `SSH_PRIVATE_KEY` | 部署私钥，**必须以换行符结尾**（缺尾换行会导致 webfactory/ssh-agent 报错） |
| `DEPLOY_PATH` | 服务器站点目录，如 `/var/www/myblog`，**必须与 nginx 的 root 一致** |

## 2. GitHub Pages 来源

仓库 Settings → Pages → Source 选择 **GitHub Actions**（一次性；未设置时 `deploy-pages` 任务会失败）。

## 3. 服务器一次性准备

```bash
mkdir -p /var/www/myblog
# 将 blog/deploy/nginx-myblog.conf 放到 /etc/nginx/conf.d/ 后重载
cp blog/deploy/nginx-myblog.conf /etc/nginx/conf.d/myblog.conf
nginx -s reload
# 把与 SSH_PRIVATE_KEY 配对的公钥加入部署用户的 authorized_keys
```

## 4. 触发方式

- push 到 `master` 且 `blog/**` 有改动时自动双部署。
- `workflow_dispatch` 仅在 workflow 已合并到 `master` 后才会出现在 Actions 页面，可手动重跑。
