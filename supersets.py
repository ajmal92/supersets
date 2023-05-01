import requests
import json

base_url = "https://analytics.ci.ccctechcenter.org/api/v1/"

payload = json.dumps({
  "password": "admin",
  "username": "admin@superset.com",
  "refresh": True,
  "provider": "db"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", f"{base_url}/security/login", headers=headers, data=payload)

access_token = response.json()['access_token']
headers['Authorization'] = f'Bearer {access_token}'
response = requests.request("GET", f"{base_url}/security/csrf_token", headers=headers)

csrf_token = response.json()['result'] nb 3
print(access_token)
print(csrf_token)

DASHBOARD_FILE_PATH = "C:\GIT\superset\config\sindhu_test.zip"

headers = {
  'Content-Type': 'application/json',
  'X-CSRFToken' :csrf_token
}

with open(DASHBOARD_FILE_PATH, 'rb') as f:
    dashboard_zip_content = f.read()
    
files={
        'file': ('dashboard.zip', dashboard_zip_content)
    }
resp = requests.request("POST", f"{base_url}/dashboard/import", headers=headers, files=files)

print(resp.status_code)
print(resp.json())