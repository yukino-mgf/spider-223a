import os
import re
import requests

url = "https://copymanga.com"
response = requests.get(url)
with open("sample.html","wb") as f:
    f.write(response.content)
