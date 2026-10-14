# Cloud Ready Status App
Flask service demonstrating health/readiness endpoints, environment configuration, Gunicorn, and a non-root Docker container.

Local run:
```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py
```
Visit `http://127.0.0.1:8000/health`.

Docker:
```bash
docker build -t razaqlabs-status .
docker run --rm -p 8000:8000 -e APP_NAME="Razaq Portfolio Status" razaqlabs-status
```
Upgrade with JSON logging, integration tests, dependency scanning, and deployment documentation. Never commit secrets.
