import requests
r=requests.get("https://gitee.com/ntkernel/irobotq/raw/master/main.py")
print(r.content.decode())
input()
