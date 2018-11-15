import requests
r=requests.get("https://raw.githubusercontent.com/ntkernel/irobotq/master/main.py")
print(r.content.decode())
input()
