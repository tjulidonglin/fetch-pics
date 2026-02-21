#!/usr/bin/env python3
"""
贪吃蛇游戏 - Flask Web 版本
"""

from flask import Flask, render_template_string, jsonify
import json
import os

app = Flask(__name__)

# HTML 模板 - 贪吃蛇游戏界面
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>贪吃蛇游戏 - Snake Game</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            padding: 30px;
            text-align: center;
            max-width: 800px;
            width: 100%;
        }

        h1 {
            color: #333;
            margin-bottom: 10px;
            font-size: 2.5em;
        }

        .subtitle {
            color: #666;
            margin-bottom: 30px;
            font-size: 1.1em;
        }

        .game-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 20px;
        }

        #gameCanvas {
            border: 3px solid #667eea;
            border-radius: 10px;
            background: #f0f0f0;
            cursor: pointer;
        }

        .score-container {
            display: flex;
            justify-content: space-between;
            width: 100%;
            margin-bottom: 10px;
        }

        .score-box {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px 30px;
            border-radius: 10px;
            min-width: 150px;
            text-align: center;
        }

        .score-box h3 {
            font-size: 0.9em;
            margin-bottom: 5px;
            opacity: 0.9;
        }

        .score-box .score-value {
            font-size: 2em;
            font-weight: bold;
        }

        .controls {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
        }

        button {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 25px;
            font-size: 1em;
            cursor: pointer;
            transition: transform 0.2s, box-shadow 0.2s;
            font-weight: bold;
        }

        button:hover {
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
        }

        button:active {
            transform: translateY(0);
        }

        .control-btn {
            padding: 15px 25px;
        }

        .game-info {
            margin-top: 20px;
            padding: 15px;
            background: #f8f9fa;
            border-radius: 10px;
            text-align: left;
        }

        .game-info h4 {
            color: #333;
            margin-bottom: 10px;
        }

        .game-info ul {
            color: #666;
            text-align: left;
            margin-left: 20px;
        }

        @media (max-width: 600px) {
            .container {
                padding: 20px;
            }

            h1 {
                font-size: 1.8em;
            }

            .controls {
                flex-direction: column;
                width: 100%;
            }

            button {
                width: 100%;
            }
        }

        .game-over {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            z-index: 100;
            display: none;
        }

        .game-over h2 {
            font-size: 3em;
            margin-bottom: 20px;
            color: #ff4444;
        }

        .game-over p {
            font-size: 1.5em;
            margin-bottom: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🐍 贪吃蛇游戏</h1>
        <p class="subtitle">经典贪吃蛇 - 用键盘方向键控制</p>

        <div class="game-container">
            <div class="score-container">
                <div class="score-box">
                    <h3>当前分数</h3>
                    <div class="score-value" id="score">0</div>
                </div>
                <div class="score-box">
                    <h3>最高分</h3>
                    <div class="score-value" id="highScore">0</div>
                </div>
            </div>

            <canvas id="gameCanvas" width="400" height="400"></canvas>

            <div class="controls">
                <button class="control-btn" onclick="startGame()">▶️ 开始游戏</button>
                <button class="control-btn" onclick="pauseGame()">⏸️ 暂停</button>
                <button class="control-btn" onclick="restartGame()">🔄 重新开始</button>
            </div>

            <div class="game-info">
                <h4>🎮 游戏说明：</h4>
                <ul>
                    <li>使用键盘方向键 <kbd>↑</kbd> <kbd>↓</kbd> <kbd>←</kbd> <kbd>→</kbd> 控制蛇的方向</li>
                    <li>吃掉食物后蛇会变长并获得分数</li>
                    <li>撞到墙壁或自己的身体游戏结束</li>
                    <li>按空格键可以暂停/继续游戏</li>
                </ul>
            </div>
        </div>
    </div>

    <div class="game-over" id="gameOverPanel">
        <h2>GAME OVER</h2>
        <p>你的分数: <span id="finalScore">0</span></p>
        <button onclick="restartGame()" style="padding: 15px 40px; font-size: 1.2em;">🎮 再来一局</button>
    </div>

    <script>
        // 游戏配置
        const GRID_SIZE = 20;
        const GRID_WIDTH = 400 / GRID_SIZE;
        const GRID_HEIGHT = 400 / GRID_SIZE;
        const GAME_SPEED = 150; // 毫秒

        // 游戏状态
        let snake = [];
        let food = {};
        let direction = 'RIGHT';
        let nextDirection = 'RIGHT';
        let score = 0;
        let highScore = localStorage.getItem('snake_highscore') || 0;
        let gameInterval;
        let gameRunning = false;
        let gamePaused = false;

        const canvas = document.getElementById('gameCanvas');
        const ctx = canvas.getContext('2d');

        // 初始化
        function init() {
            document.getElementById('highScore').textContent = highScore;
            drawGrid();
            document.addEventListener('keydown', handleKeyPress);
            canvas.addEventListener('click', startGame);
        }

        // 绘制网格
        function drawGrid() {
            ctx.clearRect(0, 0, canvas.width, canvas.height);
            ctx.fillStyle = '#f0f0f0';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
        }

        // 生成随机食物
        function generateFood() {
            food = {
                x: Math.floor(Math.random() * GRID_WIDTH),
                y: Math.floor(Math.random() * GRID_HEIGHT)
            };

            // 确保食物不会出现在蛇身上
            for (let segment of snake) {
                if (segment.x === food.x && segment.y === food.y) {
                    return generateFood();
                }
            }
        }

        // 绘制蛇
        function drawSnake() {
            snake.forEach((segment, index) => {
                if (index === 0) {
                    // 蛇头
                    ctx.fillStyle = '#4CAF50';
                } else {
                    // 蛇身
                    ctx.fillStyle = '#8BC34A';
                }
                ctx.fillRect(segment.x * GRID_SIZE, segment.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);

                // 绘制蛇身边框
                ctx.strokeStyle = '#2E7D32';
                ctx.strokeRect(segment.x * GRID_SIZE, segment.y * GRID_SIZE, GRID_SIZE, GRID_SIZE);
            });
        }

        // 绘制食物
        function drawFood() {
            // 绘制圆形食物
            ctx.fillStyle = '#FF5722';
            ctx.beginPath();
            const centerX = food.x * GRID_SIZE + GRID_SIZE / 2;
            const centerY = food.y * GRID_SIZE + GRID_SIZE / 2;
            ctx.arc(centerX, centerY, GRID_SIZE / 2 - 2, 0, Math.PI * 2);
            ctx.fill();

            // 绘制食物高光
            ctx.fillStyle = '#FF9800';
            ctx.beginPath();
            ctx.arc(centerX - 3, centerY - 3, GRID_SIZE / 6, 0, Math.PI * 2);
            ctx.fill();
        }

        // 移动蛇
        function moveSnake() {
            direction = nextDirection;

            const head = { ...snake[0] };

            switch (direction) {
                case 'UP':
                    head.y -= 1;
                    break;
                case 'DOWN':
                    head.y += 1;
                    break;
                case 'LEFT':
                    head.x -= 1;
                    break;
                case 'RIGHT':
                    head.x += 1;
                    break;
            }

            // 检查是否撞墙
            if (head.x < 0 || head.x >= GRID_WIDTH || head.y < 0 || head.y >= GRID_HEIGHT) {
                gameOver();
                return;
            }

            // 检查是否撞到自己
            for (let i = 0; i < snake.length; i++) {
                if (snake[i].x === head.x && snake[i].y === head.y) {
                    gameOver();
                    return;
                }
            }

            snake.unshift(head);

            // 检查是否吃到食物
            if (head.x === food.x && head.y === food.y) {
                score += 10;
                document.getElementById('score').textContent = score;

                // 更新最高分
                if (score > highScore) {
                    highScore = score;
                    localStorage.setItem('snake_highscore', highScore);
                    document.getElementById('highScore').textContent = highScore;
                }

                generateFood();
            } else {
                snake.pop();
            }

            // 重新绘制
            drawGrid();
            drawSnake();
            drawFood();
        }

        // 处理键盘输入
        function handleKeyPress(e) {
            if (!gameRunning) return;

            switch (e.key) {
                case 'ArrowUp':
                    if (direction !== 'DOWN') nextDirection = 'UP';
                    break;
                case 'ArrowDown':
                    if (direction !== 'UP') nextDirection = 'DOWN';
                    break;
                case 'ArrowLeft':
                    if (direction !== 'RIGHT') nextDirection = 'LEFT';
                    break;
                case 'ArrowRight':
                    if (direction !== 'LEFT') nextDirection = 'RIGHT';
                    break;
                case ' ':
                    // 空格键暂停/继续
                    if (gamePaused) {
                        resumeGame();
                    } else {
                        pauseGame();
                    }
                    break;
            }
        }

        // 开始游戏
        function startGame() {
            if (gameRunning && !gamePaused) return;

            if (!gameRunning) {
                // 初始化游戏
                snake = [{ x: 10, y: 10 }];
                direction = 'RIGHT';
                nextDirection = 'RIGHT';
                score = 0;
                document.getElementById('score').textContent = score;
                generateFood();
                drawGrid();
                drawSnake();
                drawFood();
            }

            gameRunning = true;
            gamePaused = false;

            // 清除之前的定时器
            if (gameInterval) clearInterval(gameInterval);

            // 开始游戏循环
            gameInterval = setInterval(moveSnake, GAME_SPEED);

            document.getElementById('gameOverPanel').style.display = 'none';
        }

        // 暂停游戏
        function pauseGame() {
            if (!gameRunning || gamePaused) return;
            gamePaused = true;
            clearInterval(gameInterval);
        }

        // 继续游戏
        function resumeGame() {
            if (!gameRunning || !gamePaused) return;
            gamePaused = false;
            gameInterval = setInterval(moveSnake, GAME_SPEED);
        }

        // 重新开始
        function restartGame() {
            clearInterval(gameInterval);
            gameRunning = false;
            gamePaused = false;
            startGame();
        }

        // 游戏结束
        function gameOver() {
            clearInterval(gameInterval);
            gameRunning = false;
            document.getElementById('finalScore').textContent = score;
            document.getElementById('gameOverPanel').style.display = 'block';
        }

        // 初始化游戏
        init();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/highscore', methods=['GET'])
def get_highscore():
    highscore = 0
    if os.path.exists('highscore.json'):
        with open('highscore.json', 'r') as f:
            data = json.load(f)
            highscore = data.get('highscore', 0)
    return jsonify({'highscore': highscore})

@app.route('/api/highscore', methods=['POST'])
def save_highscore():
    from flask import request
    data = request.get_json()
    highscore = data.get('highscore', 0)

    with open('highscore.json', 'w') as f:
        json.dump({'highscore': highscore}, f)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
