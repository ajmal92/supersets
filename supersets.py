import requests
import json
import argparse
import subprocess
import tempfile




def options():
    parser = argparse.ArgumentParser(description='Streamsets CI/CD script')
    parser.add_argument('-base_url', default='base_url', required=True)
    parser.add_argument('-username', help='Username', required=True)
    parser.add_argument('-password', help='password', required=True)
    args = parser.parse_args()
    return args

args = options()
  
base_url = args.base_url

payload = json.dumps({
  "password": args.password,
  "username": args.username,
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

csrf_token = response.json()['result']

base_path = "config"
temp_dir = tempfile.gettempdir()
zip_dashboard_path = os.path.join(temp_dir, 'supersets')
subprocess.run(['mkdir','-p', zip_dashboard_path)
headers = {
  'Content-Type': 'application/json',
  'X-CSRFToken' :csrf_token
}

for folder in os.listdir(f"{config}/"):
  dashboard_file_path = os.path.join(zip_dashboard_path, folder) + ".zip"
  subprocess.run(['zip', '-r', dashboard_file_path, folder], cwd=zip_dashboard_path)
  with open(dashboard_file_path, 'rb') as f:
      dashboard_zip_content = f.read()

  files={
          'file': ('dashboard.zip', dashboard_zip_content)
      }
  resp = requests.request("POST", f"{base_url}/dashboard/import", headers=headers, files=files)
  assert resp.status_code == 201
