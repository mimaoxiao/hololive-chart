#导入模块
import json
import requests
 
#模拟浏览器
headers = {
  'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
}
#包含待爬取信息的url
url = 'https://api.bilibili.com/x/relation/stat?vmid=332704117'
#访问url
r = requests.get(url,headers)
#将爬取道德json格式的数据转化为字典
text = json.loads(r.text)
print(text)
#取出嵌套字典里我们想要的部分
#这里的字典嵌套在控制台里其实看的很清楚，我在上面的截图里圈了出来
res = text['data']['follower']
with open('wlg.txt','a+',encoding="utf-8") as f:
    f.write(str(res))