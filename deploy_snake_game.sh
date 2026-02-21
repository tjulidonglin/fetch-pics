#!/bin/bash

echo "======================================"
echo "  贪吃蛇游戏 - Nginx 部署脚本"
echo "======================================"
echo ""

# 检查是否以 root 用户运行
if [ "$EUID" -ne 0 ]; then
    echo "❌ 请以 root 用户运行此脚本"
    exit 1
fi

echo "✅ 步骤 1: 安装 Python 依赖..."
pip3 install -r /root/fetch-pics/requirements.txt
echo ""

echo "✅ 步骤 2: 配置 Nginx..."
cp /root/fetch-pics/nginx_snake_game.conf /etc/nginx/sites-available/snake_game

if [ ! -f /etc/nginx/sites-enabled/snake_game ]; then
    ln -s /etc/nginx/sites-available/snake_game /etc/nginx/sites-enabled/
fi

echo ""

echo "✅ 步骤 3: 重启 Nginx..."
nginx -t
if [ $? -eq 0 ]; then
    systemctl restart nginx
    echo "✅ Nginx 配置成功并重启"
else
    echo "❌ Nginx 配置测试失败，请检查配置文件"
    exit 1
fi
echo ""

echo "✅ 步骤 4: 设置并启动 Snake Game 服务..."
cp /root/fetch-pics/snake_game.service /etc/systemd/system/

systemctl daemon-reload
systemctl enable snake_game
systemctl restart snake_game

echo ""

echo "✅ 步骤 5: 检查服务状态..."
systemctl status snake_game --no-pager -l

echo ""
echo "======================================"
echo "  🎮 部署完成！"
echo "======================================"
echo ""
echo "访问地址: http://localhost"
echo "或通过服务器 IP 访问: http://<your-server-ip>"
echo ""
echo "服务管理命令:"
echo "  启动:   systemctl start snake_game"
echo "  停止:   systemctl stop snake_game"
echo "  重启:   systemctl restart snake_game"
echo "  状态:   systemctl status snake_game"
echo ""
echo "如需停止服务并卸载:"
echo "  1. systemctl stop snake_game"
echo "  2. systemctl disable snake_game"
echo "  3. rm /etc/systemd/system/snake_game.service"
echo "  4. rm /etc/nginx/sites-available/snake_game"
echo "  5. rm /etc/nginx/sites-enabled/snake_game"
echo "  6. systemctl restart nginx"
echo ""
