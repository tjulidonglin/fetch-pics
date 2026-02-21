# 🎮 贪吃蛇游戏 - 快速使用指南

## ✨ 项目完成！已为您准备好了以下内容：

### 📦 创建的文件
1. ✅ `snake_game.py` - 完整的贪吃蛇游戏（Flask + HTML5 Canvas）
2. ✅ `requirements.txt` - Python 依赖文件
3. ✅ `nginx_snake_game.conf` - Nginx 配置文件
4. ✅ `snake_game.service` - systemd 服务配置
5. ✅ `deploy_snake_game.sh` - 一键部署脚本
6. ✅ `test_snake_game.sh` - 快速测试脚本
7. ✅ `README_SNAKE_GAME.md` - 详细文档
8. ✅ `README.md` - 项目总览
9. ✅ `DEPLOYMENT_CHECKLIST.md` - 部署检查清单

## 🚀 两种运行方式

### 方式一：快速测试（推荐先测试）

```bash
cd /root/fetch-pics
./test_snake_game.sh
```

然后在浏览器中打开：**http://localhost:5000**

✅ 无需配置，一键运行
✅ 适合开发和测试
✅ 按 Ctrl+C 停止服务

---

### 方式二：Nginx 部署（生产环境）

```bash
cd /root/fetch-pics
sudo ./deploy_snake_game.sh
```

部署完成后访问：**http://localhost**

✅ 80 端口直接访问
✅ systemd 自动管理
✅ 开机自启动
✅ 稳定可靠

---

## 🎮 游戏功能

### 控制方式
- **方向键** ↑ ↓ ← →：控制蛇的移动
- **空格键**：暂停/继续游戏
- **开始按钮**：开始新游戏
- **暂停按钮**：暂停游戏
- **重新开始按钮**：重新开始

### 游戏规则
- 吃掉红色食物获得 10 分
- 蛇会随着吃食物变长
- 撞到墙壁或自己的身体游戏结束
- 最高分会自动保存

---

## 🔧 部署后管理

### 启动/停止服务
```bash
sudo systemctl start snake_game    # 启动
sudo systemctl stop snake_game     # 停止
sudo systemctl restart snake_game   # 重启
sudo systemctl status snake_game    # 状态
```

### 查看日志
```bash
sudo journalctl -u snake_game -f   # 实时日志
```

### 卸载游戏
```bash
# 停止服务
sudo systemctl stop snake_game
sudo systemctl disable snake_game

# 删除配置
sudo rm /etc/systemd/system/snake_game.service
sudo rm /etc/nginx/sites-available/snake_game
sudo rm /etc/nginx/sites-enabled/snake_game

# 重启服务
sudo systemctl daemon-reload
sudo systemctl restart nginx
```

---

## 📊 技术特点

### 前端
- ✨ 美观的渐变色界面
- 🎨 使用 HTML5 Canvas 渲染
- 📱 响应式设计（支持移动端）
- 🎯 平滑的动画效果

### 后端
- 🐍 Python Flask 框架
- 📡 RESTful API 支持
- 💾 最高分持久化存储
- 🔄 自动重连机制

### 部署
- 🚀 Nginx 反向代理
- 🔧 systemd 服务管理
- 🔄 自动重启保护
- 📈 生产环境就绪

---

## 🐛 常见问题

### 1. 无法访问游戏页面
```bash
# 检查服务状态
sudo systemctl status snake_game

# 检查 Nginx
sudo systemctl status nginx

# 检查端口
netstat -tlnp | grep -E '80|5000'
```

### 2. 部署脚本报错
```bash
# 确保有执行权限
chmod +x deploy_snake_game.sh

# 使用 sudo 运行
sudo ./deploy_snake_game.sh
```

### 3. 游戏卡顿或延迟
编辑 `snake_game.py`，调整游戏速度：
```javascript
const GAME_SPEED = 200;  // 增大数值降低难度
```

---

## 🎉 开始游戏！

选择你喜欢的方式，立即开始游戏吧！

**快速测试**: `./test_snake_game.sh`
**生产部署**: `sudo ./deploy_snake_game.sh`

---

## 📝 注意事项

- 部署脚本需要 root 权限
- 确保 80 端口未被占用
- 防火墙可能需要开放 80 端口
- 最高分保存在本地浏览器中

---

**祝你游戏愉快！** 🎮🐍
