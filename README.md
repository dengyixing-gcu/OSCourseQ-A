# 操作系统课程知识问答智能体

《操作系统》课程本科学生自学辅助工具，覆盖设备管理（第7章）和文件管理（第8章）两大核心模块。

## 功能特性

- **智能问答**：接入智谱AI大模型，支持自然语言提问
- **知识导航**：热门话题快捷入口，方便快速开始
- **双章覆盖**：设备管理（I/O管理、磁盘管理、缓冲管理）和文件管理（文件系统、目录、保护机制）
- **磁盘调度计算**：交互式计算器，支持FCFS/SSTF/SCAN/C-SCAN/LOOK/C-LOOK算法
- **安全代理**：API Key存储在服务器端，不暴露在前端代码中

## 使用方法

1. 直接打开 `index.html` 文件
2. 在输入框中用自然语言提问
3. 点击发送或按回车键获取答案
4. 点击顶部标签切换章节（设备管理/文件管理/磁盘调度计算）

## 部署架构

```
前端 (GitHub Pages)          代理服务器 (Render/Railway)
┌─────────────────┐         ┌─────────────────────────┐
│   index.html    │ ──POST──▶ │  Flask Proxy Server     │
│   纯静态页面     │         │  ZHIPU_API_KEY (环境变量) │
└─────────────────┘         └──────────┬──────────────┘
                                       │ POST
                                       ▼
                              ┌─────────────────────────┐
                              │   智谱AI API             │
                              │   open.bigmodel.cn       │
                              └─────────────────────────┘
```

## 代理服务器部署

API Key通过代理服务器安全保管，不暴露在前端代码中。

### 快速部署到Render（免费）

1. 访问 https://render.com 注册账号
2. 点击 "New +" → "Web Service"
3. 连接GitHub仓库 `OSCourseQ-A`
4. 配置：
   - **Root Directory**: `proxy`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn server:app`
   - **Environment Variables**: 添加 `ZHIPU_API_KEY` = 你的API Key
5. 部署完成后，复制服务URL
6. 修改 `index.html` 第146行的 `PROXY_URL` 为你的代理服务器URL

### 本地运行（开发测试）

```bash
cd proxy
pip install -r requirements.txt
export ZHIPU_API_KEY="你的API Key"
python server.py
```

详细部署说明见 [proxy/README.md](proxy/README.md)

## 知识覆盖

### 第7章 设备管理
- 7.1 I/O管理概述
- 7.2 I/O控制方式
- 7.3 I/O系统
- 7.4 磁盘管理
- 7.5 缓冲管理

### 第8章 文件管理
- 8.1 文件概述
- 8.2 文件结构和文件系统
- 8.3 目录
- 8.4 文件系统实现
- 8.5 文件系统可靠性
- 8.6 保护机制

## License

MIT
