import requests

url = "https://ipinfo.io/ip"

for i in range(1, 101):
    try:
        response = requests.get(url, timeout=5)
        print(f"{i}: 状态码 {response.status_code}")
    except requests.RequestException as e:
        print(f"{i}: 请求失败 {e}")
