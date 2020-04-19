#导入模块
import json
import requests

headers = {
  'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}

file = open('bid.json','r',encoding='utf-8')
info = json.load(file)
length=len(info['data'])
result='['

for i in range(length):
  
  if(i!=0):
    result+=','
  
  url = 'https://api.bilibili.com/x/relation/stat?vmid='+info['data'][i]['bid']

  r = requests.get(url,headers)

  text = json.loads(r.text)
  result += str(text['data']['follower'])

result+=']'

with open('data.txt','w+',encoding="utf-8") as f:
  f.write(result)