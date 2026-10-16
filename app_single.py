from flask import Flask

# 1. 建立 Flask 核心應用實例
app = Flask(__name__)

# 2. 定義首頁路由與視圖函數
@app.route('/')
def hello_world():
    # 直接回傳 HTML 標籤的一頁式網頁
    return """
    <!DOCTYPE html>
    <html lang="zh-Hant">
    <head>
        <meta charset="UTF-8">
        <title>Hello World - Flask</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
                background: #f0f2f5;
            }
            .card {
                background: white;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 { color: #1877f2; margin-bottom: 10px; }
            p { color: #555; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, World!</h1>
            <p>這是一個使用 Python Flask 的極簡一頁式網頁。</p>
        </div>
    </body>
    </html>
    """

# 3. 啟動伺服器
if __name__ == '__main__':
    app.run(debug=True, port=5000)
