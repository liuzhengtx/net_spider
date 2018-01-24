# -*- coding:utf-8 -*-
"""""""""
   File Name：     get_dianying_movie
   Description :    将电影天堂里的所有迅雷链接存放到一个文本文件中
   Author :       liuzhengtx
   date：          2018/1/24
"""""""""
import requests, re, time


class Downloader_dytt_movie(object):
    def __init__(self):
        self.target =[]#存放每一页的url(该页包含很多电影资源)
        self.server='http://www.dytt8.net/html/gndy/dyzz/list_23_%d.html'
        self.page_url=[]#存放每个电影的url（该页只包含一个电影资源）
        self.url=[]#将提取到的电影url统一存放

    def get_movie_gage(self):#得到包含每一页包含很多电影资源的url
        for n in range(1,169):
            self.target.append(self.server%n)

    def get_movie_gage_url(self):#得到具体一部电影的url
        n=0
        for n in range(len(self.target)):#可以自己定义所要爬的页面数
            req = requests.get(url=self.target[n])  # 网络请求
            req.encoding = 'gb2312'  # 编码格式
            url_page=re.findall('href="(.*?)" class="ulink">',req.text)#正则查找，万能的（.*？）
            n+=len(url_page)
            url_base='http://www.dytt8.net'
            for m in range(len(url_page)):
                self.page_url.append(url_base+url_page[m])

    def get_downloader_url(self):#得到所有的电影的迅雷链接
        for n in range(len(self.page_url)):
            req=requests.get(self.page_url[n])
            req.encoding='gb2312'
            ftp=re.findall('td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(.*?)">',req.text)
            for n in range(len(ftp)):
                self.url.append(ftp[n])
                print(self.url)

    def url_save(self):#将得到的链接存放到txt文本
        with open('dytt.txt','w',encoding='utf-8')as f:#编码格式要写，不然会报错
            for i in self.url:
                f.write(i)
                f.write('\n')
                f.flush()

if __name__ == '__main__':
    gl = Downloader_dytt_movie()
    gl.get_movie_gage()
    gl.get_movie_gage_url()
    gl.get_downloader_url()
    gl.url_save()