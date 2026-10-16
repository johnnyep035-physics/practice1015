# Flask Hello World 一頁式網頁範例

這是一個使用 Python Flask 框架建置的輕量級一頁式（Single Page）網頁範例。

## 專案結構
```text
practice 1015/
│
├── app.py              # Flask 後端應用主程式
├── requirements.txt    # 套件依賴清單
└── templates/
    └── index.html      # 前端一頁式網頁模板（含樣式與互動腳本）
```

## 執行步驟

### 1. 安裝套件（若尚未安裝）
```bash
pip install -r requirements.txt
```

### 2. 啟動伺服器
```bash
python app.py
```

### 3. 開啟網頁
在瀏覽器網址列輸入：
```text
http://127.0.0.1:5000/
```
即可看到 Hello World 頁面！
