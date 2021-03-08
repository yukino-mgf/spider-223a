import os
import re
import requests

url = "https://copymanga.com"
response = requests.get(url)
with open("sample2.html","wb") as f:
    f.write(response.content)

# result_urls = []
result_urls = re.findall(r'href="(.*?)"',response.text)
result_urls+=re.findall(r'data-src="(.*?)"',response.text)
result_urls+=re.findall(r'url[(]"(.*?)"[)]',response.text)
with open('./log/url.txt','w') as f:
    for response_url in result_urls:
        f.write(response_url+'\n')
print(result_urls)