import logging, os
from flask import Flask, jsonify, render_template_string
logging.basicConfig(level=os.getenv('LOG_LEVEL','INFO'))
app=Flask(__name__); NAME=os.getenv('APP_NAME','Cloud Ready Status App')
HTML="""<!doctype html><html lang='en'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width, initial-scale=1'><title>{{ name }}</title><style>body{font-family:system-ui;background:#101827;color:#f5f7fb;display:grid;place-items:center;min-height:100vh;margin:0}main{max-width:650px;margin:24px;padding:32px;border:1px solid #344258;border-radius:20px;background:#182338}code,.status{color:#9de1d0}</style></head><body><main><p class='status'>● Service running</p><h1>{{ name }}</h1><p>A container-ready Flask app with health checks and environment configuration.</p><p>Health endpoint: <code>/health</code></p><p>Version: <code>{{ version }}</code></p></main></body></html>"""
@app.get('/')
def home(): return render_template_string(HTML,name=NAME,version=os.getenv('APP_VERSION','1.0.0'))
@app.get('/health')
def health(): return jsonify(status='ok',app=NAME)
@app.get('/ready')
def ready(): return jsonify(ready=True)
if __name__=='__main__': app.run(host='0.0.0.0',port=int(os.getenv('PORT','8000')))
