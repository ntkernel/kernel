import requests
r=requests.get("https://gitee.com/ntkernel/irobotq/raw/master/py.py")
print(r.content.decode())
input()
