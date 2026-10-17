# Flask Hello World 一頁式網頁範例

這是一個使用 Python Flask 框架建置的輕量級一頁式（Single Page）網頁範例，並已配置 GitHub Actions 與 Render 的 CI/CD 自動化流程。

## 專案結構
```text
practice 1015/
│
├── .github/workflows/
│   └── deploy.yml      # GitHub Actions CI/CD 工作流程設定
├── templates/
│   └── index.html      # 前端一頁式網頁模板（含樣式與互動腳本）
├── app.py              # Flask 後端應用主程式
├── app_single.py       # 單檔極簡版範例
├── render.yaml         # Render 服務規格設定檔 (Blueprint)
├── requirements.txt    # Python 套件依賴清單 (含 gunicorn)
├── test_app.py         # 自動化單元測試檔 (CI 測試用)
└── README.md           # 專案說明文件
```

---

## 本地執行步驟

### 1. 安裝套件
```bash
pip install -r requirements.txt
```

### 2. 啟動伺服器
```bash
python app.py
```

### 3. 開啟網頁
在瀏覽器輸入：
```text
http://127.0.0.1:5000/
```

### 4. 執行本地單元測試
```bash
python -m unittest test_app.py
```

---

## CI/CD 自動化部署設定 (GitHub Actions + Render)

本專案採用 **GitHub Actions 負責 CI 測試，通過後觸發 Render CD 部署** 的架構。

### 工作流程運作機制：
1. **CI 階段 (test)**：每次 Push 或 PR 至 `main` 分支時，自動啟動 Ubuntu 虛擬機，安裝依賴並執行 `python -m unittest test_app.py` 測試。
2. **CD 階段 (deploy)**：只有在測試通過且分支為 `main` 時，呼叫 Render 的 Deploy Hook 進行零停機自動更新部署。

---

### 如何完成 Render 與 GitHub 串接？

#### 第一步：在 Render 上建立 Web Service
1. 登入 [Render](https://render.com/)。
2. 點擊右上角 **New +** > **Web Service**（或 **Blueprint** 並選取此專案 GitHub 倉庫）。
3. 連接您的 GitHub 專案 `johnnyep035-physics/practice1015`。
4. 設定參數：
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Auto-Deploy**: 建議設為 **No**（這樣部署權限將完全交由 GitHub Actions CI 測試把關）。

#### 第二步：取得 Deploy Hook 網址
1. 在 Render 服務頁面點擊左側 **Settings**。
2. 向下滾動至 **Deploy Hook** 區塊。
3. 點擊 **Add Deploy Hook** 或直接複製生成的 Hook 網址（格式如：`https://api.render.com/deploy/srv-xxxxxxx?key=yyyyyy`）。

#### 第三步：將 Deploy Hook 設定至 GitHub Secrets
1. 開啟您的 GitHub 專案：[practice1015](https://github.com/johnnyep035-physics/practice1015)。
2. 點選 **Settings** > **Secrets and variables** > **Actions**。
3. 點擊 **New repository secret**：
   - **Name**: `RENDER_DEPLOY_HOOK_URL`
   - **Secret**: 貼上剛剛在 Render 複製的 Deploy Hook 完整網址。
4. 點擊 **Add secret** 完成儲存。

完成後，每次推送到 `main` 分支，GitHub Actions 將會先跑測試，測試綠燈時便會自動通知 Render 進行部署！
