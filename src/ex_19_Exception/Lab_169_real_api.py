import requests

try:
    url = input("Enter URL: ")
    response = requests.get(url,timeout=3)
    print(response.status_code)
except requests.exceptions.ConnectionError:
    print("Connection error-due to wrong URL or connection fail")
except requests.exceptions.Timeout:
    print("time out error,not able to load the URL")
except Exception as e:
    print(e)