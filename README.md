[03_ai_protocols/01_mcp/04_fundamental_ primitives/01_hello_mcp_server/postman/Hello_MCP_Server.postman_collection.json:](https://github.com/panaversity/learn-agentic-ai/blob/main/03_ai_protocols/01_mcp/04_fundamental_%20primitives/01_hello_mcp_server/postman/Hello_MCP_Server.postman_collection.json)

MCP command: Press CTRL+C to quit

uv init hello-mcp
cd hello-mcp

Delete and create virtual environment run:
uv venv
or: uv sync

uv add mcp_server

uv add mcp uvicorn httpx

then Add requests:
uv add requests

optional Add server file.py from git and run :
uv run uvicorn server:mcp_app --port 8000 --reload

next Add main.py and code and run:
uv run uvicorn main:mcp_app
 
next Add client file.py from git and run:
uv run client.py

Press CTRL+C to quit.

POST MANcommannd

open postman dash board click new request
click post  add ur local url:http://localhost:8000/mcp

add headers new in bottem Accept tab and add:application/json,text/event-stream

open body and add in raw tab:
{
    "id": "1",
    "method": "tools/list",
    "params": {},
    "jsonrpc": "2.0"
}

click send and check output in bottom.
200 OK means your server working

next step goto collection click at impot add your file as your alreay add or past there




Hello_MCP_Server.postman_collection.json:
{
	"info": {
		"name": "Hello MCP Server",
		"description": "Educational Postman collection for testing MCP servers, following the 2025-06-18 specification. Demonstrates the full stateful lifecycle: initialization, tool discovery, and execution.",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json"
	},
	"item": [
		{
			"name": "01. Initialize Session",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					},
					{
						"key": "Accept",
						"value": "application/json, text/event-stream"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"initialize\",\n    \"params\": {\n        \"protocolVersion\": \"2025-06-18\",\n        \"clientInfo\": {\n            \"name\": \"postman-client\",\n            \"version\": \"1.0.0\"\n        },\n        \"capabilities\": {}\n    },\n    \"id\": 1\n}"
				},
				"url": {
					"raw": "{{baseUrl}}/mcp/",
					"host": [
						"{{baseUrl}}"
					],
					"path": [
						"mcp",
						""
					]
				},
				"description": "Initialize the MCP server connection. This is the first step in any MCP session, establishing the protocol version and exchanging capabilities. Even for simple interactions, this is a required step in the protocol."
			}
		},
		{
			"name": "02. Send Initialized Notification",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					},
					{
						"key": "Accept",
						"value": "application/json, text/event-stream"
					},
					{
						"key": "MCP-Protocol-Version",
						"value": "2025-06-18"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"notifications/initialized\",\n    \"params\": {}\n}"
				},
				"url": {
					"raw": "{{baseUrl}}/mcp/",
					"host": [
						"{{baseUrl}}"
					],
					"path": [
						"mcp",
						""
					]
				},
				"description": "Send the initialized notification to complete the MCP session setup. This is required by the 2025-06-18 specification after receiving a successful initialize response."
			}
		},
		{
			"name": "03. List Available Tools",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Content-Type",
						"value": "application/json"
					},
					{
						"key": "Accept",
						"value": "application/json, text/event-stream"
					},
					{
						"key": "MCP-Protocol-Version",
						"value": "2025-06-18"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"jsonrpc\": \"2.0\",\n    \"method\": \"tools/list\",\n    \"params\": {},\n    \"id\": 3\n}"
				},
				"url": {
					"raw": "{{baseUrl}}/mcp/",
					"host": [
						"{{baseUrl}}"
					],
					"path": [
						"mcp",
						""
					]
				},
				"description": "Discover what tools the MCP server provides. Note the 'MCP-Protocol-Version' header, required by the spec for all requests after initialization."
			}
		}
	],
	"variable": [
		{
			"key": "baseUrl",
			"value": "http://localhost:8000"
		}
	]
} 