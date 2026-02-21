# Fetch Pics 项目

本项目包含两个独立的功能模块：

## 📸 Instagram 图片下载器

一个用于学习目的的 Instagram 图片下载工具。

- **文件**: `instagram_image_downloader.py`
- **文档**: [README_instagram.md](README_instagram.md)
- **用途**: 学习 Web 抓取、HTTP 请求和 API 交互

⚠️ **注意**: 此工具仅供学习使用，请遵守 Instagram 服务条款和相关法律法规。

## 🐍 贪吃蛇游戏

一个基于 Web 的经典贪吃蛇游戏，具有美观的界面和完整的功能。

### 🚀 快速开始

#### 方式 1: 直接运行（测试用）
```bash
./test_snake_game.sh
```
然后在浏览器中访问: `http://localhost:5000`

#### 方式 2: Nginx 部署（生产环境）

使用自动部署脚本：
```bash
./deploy_snake_game.sh
```

部署完成后访问: `http://localhost` 或 `http://<你的服务器IP>`

### 📁 文件说明

- **snake_game.py** - Flask 服务器和游戏逻辑
- **requirements.txt** - Python 依赖
- **nginx_snake_game.conf** - Nginx 配置文件
- **snake_game.service** - systemd 服务配置
- **deploy_snake_game.sh** - 部署脚本
- **test_snake_game.sh** - 快速测试脚本
- **README_SNAKE_GAME.md** - 贪吃蛇游戏详细文档

### 🎮 游戏特性

- ✅ 美观的渐变色界面
- ✅ 键盘方向键控制
- ✅ 实时分数和最高分显示
- ✅ 支持暂停、重新开始
- ✅ 自动保存最高分
- ✅ 响应式设计（支持移动端）

### 🔧 技术栈

- **前端**: HTML5 Canvas, JavaScript
- **后端**: Python Flask
- **部署**: Nginx + systemd

## 📝 许可证

本项目仅供学习和娱乐使用。
