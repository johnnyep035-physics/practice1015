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
        message="歡迎來到 Python Flask 的世界！這是一個優雅簡潔的一頁式網頁範例。"
    )

if __name__ == '__main__':
    # debug=True 可在開發時開啟除錯模式，程式碼更新後會自動重載
    app.run(host='127.0.0.1', port=5000, debug=True)
