#!/bin/bash

echo "======================================"
echo "  贪吃蛇游戏 - 快速测试"
echo "======================================"
echo ""

# 检查 Flask 是否已安装
if ! python3 -c "import flask" 2>/dev/null; then
    echo "❌ Flask 未安装，正在安装..."
    pip3 install flask -q
    echo ""
fi

echo "✅ Flask 已安装"
echo ""

echo "🎮 启动贪吃蛇游戏服务器..."
echo "   访问地址: http://localhost:5000"
echo "   按 Ctrl+C 停止服务器"
echo ""
echo "在浏览器中打开上述地址即可开始游戏！"
echo ""

python3 /root/fetch-pics/snake_game.py
