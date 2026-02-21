# 🐍 贪吃蛇游戏 - Snake Game

一个基于 HTML5 Canvas 和 Flask 的经典贪吃蛇游戏，提供 Web 界面。

## 🎮 游戏特性

- 🎨 美观的渐变色界面
- ⌨️ 键盘方向键控制
- 📊 实时分数和最高分显示
- 🎯 经典贪吃蛇玩法
- 🔄 支持暂停、重新开始
- 💾 自动保存最高分

## 📦 快速开始

### 1. 安装依赖

```bash
pip3 install -r requirements.txt
```

### 2. 运行游戏服务器

```bash
python3 snake_game.py
```

### 3. 访问游戏

在浏览器中打开：`http://localhost:5000`

## 🚀 通过 Nginx 部署

### 自动部署脚本

运行部署脚本（需要 root 权限）：

```bash
chmod +x deploy_snake_game.sh
./deploy_snake_game.sh
```

部署完成后，通过以下地址访问游戏：

- 本地访问: `http://localhost`
- 服务器访问: `http://<你的服务器IP>`

### 手动部署步骤

1. **安装依赖**
   ```bash
   pip3 install flask
   ```

2. **配置 Nginx**
   ```bash
   sudo cp nginx_snake_game.conf /etc/nginx/sites-available/snake_game
   sudo ln -s /etc/nginx/sites-available/snake_game /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

3. **设置 systemd 服务**
   ```bash
   sudo cp snake_game.service /etc/systemd/system/
   sudo systemctl daemon-reload
   sudo systemctl enable snake_game
   sudo systemctl start snake_game
   ```

4. **检查服务状态**
   ```bash
   sudo systemctl status snake_game
   ```

## 🎹 游戏控制

- **方向键** ↑ ↓ ← →：控制蛇的移动方向
- **空格键**：暂停/继续游戏
- **开始按钮**：开始新游戏
- **暂停按钮**：暂停游戏
- **重新开始按钮**：重新开始游戏

## 📝 游戏规则

1. 使用方向键控制蛇的移动
2. 吃掉红色食物后蛇会变长并获得分数
3. 每吃一个食物获得 10 分
4. 撞到墙壁或自己的身体游戏结束
5. 最高分会自动保存到本地

## 🛠️ 技术栈

- **前端**: HTML5 Canvas, JavaScript
- **后端**: Python Flask
- **部署**: Nginx + systemd

## 📊 API 接口

### 获取最高分
```http
GET /api/highscore
```

### 保存最高分
```http
POST /api/highscore
Content-Type: application/json

{
    "highscore": 100
}
```

## 🔧 配置说明

### 游戏配置 (在 snake_game.py 中)

```javascript
const GRID_SIZE = 20;          // 网格大小
const GAME_SPEED = 150;        // 游戏速度（毫秒）
```

### 调整难度

- **更简单**：增大 `GAME_SPEED` 值（如 200）
- **更困难**：减小 `GAME_SPEED` 值（如 100）

## 🐛 故障排除

### Nginx 配置错误
```bash
sudo nginx -t  # 检查配置
sudo systemctl restart nginx
```

### Flask 服务无法启动
```bash
# 检查端口占用
netstat -tlnp | grep 5000

# 查看服务日志
sudo journalctl -u snake_game -f
```

### 防火墙设置
```bash
# 开放 80 端口
sudo ufw allow 80/tcp

# 或使用 iptables
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

## 📄 许可证

本项目仅供学习和娱乐使用。

## 👨‍💻 开发者

贪吃蛇游戏 - 经典重现，快乐无限！
