import os
from flask import Flask, render_template

# 建立 Flask 應用程式實例
app = Flask(__name__)

# 定義根路徑 (首頁) 的路由
@app.route('/')
def home():
    # 傳遞參數給模板呈現
    return render_template(
        'index.html',
        title="Hello World - Flask 一頁式網頁",
        heading="Hello, World!",
        message="歡迎來到 Python Flask Johnny Mia 的世界！這是一個優雅簡潔的一頁式網頁範例（CI/CD 自動部署驗證成功 🚀）。"
    )

if __name__ == '__main__':
    # 支援雲端平台 (如 Render) 動態指定的 PORT，本機預設 5000
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)

