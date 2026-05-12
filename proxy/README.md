# 代理服务器部署说明

## 方案说明

API Key存储在服务器环境变量中，前端通过代理服务器调用智谱AI API，避免API Key暴露在前端代码中。

## 部署到Render（免费）

1. 访问 https://render.com 注册账号
2. 点击 "New +" → "Web Service"
3. 连接GitHub仓库 `OSCourseQ-A`
4. 配置：
   - **Root Directory**: `proxy`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
   - **Environment Variables**: 添加 `ZHIPU_API_KEY` = 你的API Key
5. 点击 "Create Web Service"
6. 部署完成后，复制服务URL（如 `https://os-course-qa-proxy.onrender.com`）
7. 修改 `index.html` 中的 `PROXY_URL` 为你的代理服务器URL

## 部署到Railway（免费额度）

1. 访问 https://railway.app 注册账号
2. 点击 "New Project" → "Deploy from GitHub repo"
3. 选择 `OSCourseQ-A` 仓库
4. 设置Root Directory为 `proxy`
5. 在Variables中添加 `ZHIPU_API_KEY` = 你的API Key
6. 部署完成后，复制服务URL
7. 修改 `index.html` 中的 `PROXY_URL`

## 本地运行（开发测试）

```bash
cd proxy
pip install -r requirements.txt
export ZHIPU_API_KEY="你的API Key"
python server.py
```

服务将在 `http://localhost:5000` 启动。

## API接口

- `POST /api/chat` - 聊天接口
  ```json
  {
    "model": "glm-4-flash",
    "messages": [{"role": "user", "content": "你好"}],
    "temperature": 0.7,
    "max_tokens": 2048
  }
  ```

- `GET /api/health` - 健康检查
