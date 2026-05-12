from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

API_KEY = os.environ.get('ZHIPU_API_KEY')
API_URL = 'https://open.bigmodel.cn/api/paas/v4/chat/completions'

@app.route('/api/chat', methods=['POST'])
def chat():
    if not API_KEY:
        return jsonify({'error': 'API Key未配置'}), 500
    
    data = request.get_json()
    if not data or 'messages' not in data:
        return jsonify({'error': '请求格式错误'}), 400
    
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    payload = {
        'model': data.get('model', 'glm-4-flash'),
        'messages': data['messages'],
        'temperature': data.get('temperature', 0.7),
        'max_tokens': data.get('max_tokens', 2048)
    }
    
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=60)
        return jsonify(response.json()), response.status_code
    except requests.exceptions.RequestException as e:
        return jsonify({'error': str(e)}), 502

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
