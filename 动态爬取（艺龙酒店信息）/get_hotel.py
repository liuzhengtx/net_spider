import requests,re,time
from 动态网页抓取 import src
import  pandas as pd
#post请求地址
get_url = 'http://hotel.elong.com/ajax/list/asyncsearch'
#map是映射，lambda是定义一个函数，-->[str[1],str[2]..str[10]]-->['1','2'..'10']
for n in list(map(lambda x: str(x),range(1,10))):
    time.sleep(1)#短延时，避免服务器误认为为非人操作
    src.data['listRequest.pageIndex']=n#换页
    dat=requests.post(url=get_url, headers=src.headers, data=src.data)#进行post操作
    jn=dat.json()#在浏览器的开发者工具里可以看到，数据可以转为json格式
    #提取酒店名称
    hotel_name=re.findall('target="_blank" title="(.*?)"><span',jn['value']['hotelListHtml'])
    #提取酒店价格
    hotel_price=re.findall('<span class="h_pri_num ">(.*?)</span>',jn['value']['hotelListHtml'])
   #将酒店名称和价格一一对应，并转化为list格式
    a=list(map(lambda x:(hotel_name[x],hotel_price[x]) ,range(len(hotel_name))))
    b=pd.DataFrame(a)#将数据写入CSV
    b.to_csv('data.csv',header=False,index=False,mode='a',encoding='utf-8')

