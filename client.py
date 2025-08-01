import requests
url = "http://localhost:8000/mcp"

headers = {
    "Accept": "application/json,text/event-stream",
}
body = {
    "jsonrpc": "2.0",
    "method": "tools/list",
    "id": "1",
    "params": {},
}
response = requests.post(url, json=body, headers=headers)

for line in response.iter_lines():
    if line:
        print(line)

# uvicorn main:app --host 127.0.0.1 --port 8000