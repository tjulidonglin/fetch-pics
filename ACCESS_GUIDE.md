# 🎮 贪吃蛇游戏 - 公网访问指南

## ✅ 部署成功！

### 🌐 访问地址

**你的贪吃蛇游戏已经部署成功，可以通过以下地址访问：**

🌐 **公网访问**: http://47.84.118.70

📱 **手机访问**: 在手机浏览器中输入 `47.84.118.70`

---

## 🎮 游戏操作

### 键盘控制
- **↑ (上箭头)** - 向上移动
- **↓ (下箭头)** - 向下移动
- **← (左箭头)** - 向左移动
- **→ (右箭头)** - 向右移动
- **空格键** - 暂停/继续游戏

### 界面按钮
- **▶️ 开始游戏** - 开始新游戏
- **⏸️ 暂停** - 暂停当前游戏
- **🔄 重新开始** - 重新开始游戏

---

## 🎯 游戏规则

1. 使用方向键控制蛇的移动方向
2. 吃掉红色食物获得 10 分
3. 蛇会随着吃食物变长
4. 撞到墙壁或自己的身体游戏结束
5. **最高分会自动保存**（保存在浏览器中）

---

## 🔧 服务管理

### 检查服务状态
```bash
# 检查贪吃蛇游戏服务
systemctl status snake_game

# 检查 Nginx 服务
systemctl status nginx
```

### 启动/停止服务
```bash
# 启动游戏服务
sudo systemctl start snake_game

# 停止游戏服务
sudo systemctl stop snake_game

# 重启游戏服务
sudo systemctl restart snake_game
```

### 重启 Nginx
```bash
sudo systemctl restart nginx
```

---

## 📊 服务信息

### 当前运行状态
- ✅ **Nginx**: 运行中 (监听 80 端口)
- ✅ **Flask 服务**: 运行中 (监听 5000 端口)
- ✅ **systemd 服务**: 已启用（开机自启动）

### 端口配置
- **80 端口**: Nginx 反向代理
- **5000 端口**: Flask 应用服务

---

## 🔍 故障排查

### 无法访问游戏

1. **检查服务是否运行**
   ```bash
   systemctl status snake_game
   systemctl status nginx
   ```

2. **测试本地访问**
   ```bash
   curl http://localhost/
   ```

3. **测试公网访问**
   ```bash
   curl http://47.84.118.70/
   ```

4. **检查端口监听**
   ```bash
   netstat -tlnp | grep -E ":(80|5000)"
   ```

5. **查看日志**
   ```bash
   # Flask 服务日志
   sudo journalctl -u snake_game -f

   # Nginx 日志
   sudo tail -f /var/log/nginx/error.log
   ```

### 游戏页面显示异常

1. 清除浏览器缓存
2. 使用无痕模式重新访问
3. 检查浏览器控制台是否有错误

---

## 📝 重要说明

### 防火墙配置
当前防火墙状态：**未启用 (inactive)**

如果启用防火墙，需要开放 80 端口：
```bash
sudo ufw allow 80/tcp
sudo ufw enable
```

### 其他站点
- 已临时禁用 `ecommerce` 站点
- 如需恢复 ecommerce 站点，请运行：
  ```bash
  sudo ln -s /etc/nginx/sites-available/ecommerce /etc/nginx/sites-enabled/
  sudo systemctl restart nginx
  ```

---

## 🎉 开始游戏！

现在打开浏览器，访问：**http://47.84.118.70**

享受你的贪吃蛇游戏！🐍🎮

---

## 📞 技术支持

如遇到问题，可以：
1. 检查上述故障排查步骤
2. 查看服务日志获取详细信息
3. 确认服务器网络连接正常

---

**部署时间**: 2026-02-21 14:17
**服务器公网IP**: 47.84.118.70
**游戏状态**: ✅ 运行中
