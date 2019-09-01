import requests
# import json

# ========
 url_ = "https://habr.com/ru/"
 session = requests.Session()
 r = session.get(url_, timeout=5)
 print(r.text)