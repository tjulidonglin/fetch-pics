# 贪吃蛇游戏部署检查清单

## 🎮 本地测试（可选）

- [ ] 运行 `./test_snake_game.sh`
- [ ] 在浏览器中打开 `http://localhost:5000`
- [ ] 验证游戏可以正常启动
- [ ] 测试方向键控制
- [ ] 测试暂停/继续功能
- [ ] 验证分数计算正确
- [ ] 测试游戏结束功能

## 🚀 生产部署

### 前置检查

- [ ] 确认已安装 Python 3
- [ ] 确认已安装 Nginx
- [ ] 确认有 root 或 sudo 权限
- [ ] 检查 80 端口是否可用

### 自动部署

```bash
./deploy_snake_game.sh
```

### 部署后验证

- [ ] 检查 Nginx 配置: `nginx -t`
- [ ] 检查 Nginx 状态: `systemctl status nginx`
- [ ] 检查 Snake Game 服务: `systemctl status snake_game`
- [ ] 在浏览器中访问 `http://localhost`
- [ ] 测试所有游戏功能

### 防火墙配置（如需要）

- [ ] 开放 80 端口: `sudo ufw allow 80/tcp`
- [ ] 检查防火墙状态: `sudo ufw status`

## 📊 服务管理

### 启动/停止服务

```bash
# 启动
sudo systemctl start snake_game

# 停止
sudo systemctl stop snake_game

# 重启
sudo systemctl restart snake_game

# 查看状态
sudo systemctl status snake_game
```

### 查看日志

```bash
# 实时日志
sudo journalctl -u snake_game -f

# 最近 100 行日志
sudo journalctl -u snake_game -n 100
```

## 🔧 故障排除

### 游戏无法访问

1. 检查服务状态: `systemctl status snake_game`
2. 检查 Nginx 状态: `systemctl status nginx`
3. 检查端口占用: `netstat -tlnp | grep -E '80|5000'`
4. 检查防火墙: `sudo ufw status`

### Nginx 配置错误

```bash
sudo nginx -t                    # 测试配置
sudo nginx -T                    # 查看完整配置
sudo systemctl restart nginx     # 重启 Nginx
```

### 清理部署

如需卸载：

```bash
# 停止服务
sudo systemctl stop snake_game
sudo systemctl disable snake_game

# 删除配置文件
sudo rm /etc/systemd/system/snake_game.service
sudo rm /etc/nginx/sites-available/snake_game
sudo rm /etc/nginx/sites-enabled/snake_game

# 重启服务
sudo systemctl daemon-reload
sudo systemctl restart nginx

# 删除项目文件（可选）
# rm /root/fetch-pics/snake_game.py
# rm /root/fetch-pics/nginx_snake_game.conf
# rm /root/fetch-pics/snake_game.service
# rm /root/fetch-pics/deploy_snake_game.sh
# rm /root/fetch-pics/test_snake_game.sh
```

## ✅ 完成标准

- [ ] 游戏页面正常加载
- [ ] 可以开始新游戏
- [ ] 方向键控制正常
- [ ] 分数显示正确
- [ ] 暂停/继续功能正常
- [ ] 游戏结束逻辑正确
- [ ] 最高分可以保存
- [ ] 服务开机自启动
- [ ] 服务运行稳定

## 📝 备注

- 部署脚本需要 root 权限
- 默认监听 80 端口
- Flask 服务运行在 5000 端口
- Nginx 作为反向代理转发请求
- 最高分数据保存在本地浏览器和 highscore.json 文件中
