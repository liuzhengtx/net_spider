# -*- coding:utf-8 -*-
"""""""""
   File Name：     get_hero
   Description :    下载王者荣耀盒子英雄菜单里的所有英雄
   Author :       liuzhengtx
   date：          2018/1/21
"""""""""
import requests
import json
from contextlib import closing
import os

class Downloader_picture():
    def __init__(self):
        self.target = 'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90001a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.2&version_code=1202&cuid=F0BBAC7AD20D6E96797DE8D82D992985&ovr=6.0&device=Meizu_MX6&net_type=1&client_id=O4EnvUNSK7Ij7AIX6vO9fA%3D%3D&info_ms=WGLj4Jk7nrCBU3h3L4%2BHzQ%3D%3D&info_ma=UEP8WG%2B2QNZAjBYXE1px2kk9VoPw8HvtU15f%2Be1NJQU%3D&mno=0&info_la=QbpJbZVTFiMUiJLG4LvZWg%3D%3D&info_ci=QbpJbZVTFiMUiJLG4LvZWg%3D%3D&mcc=0&clientversion=&bssid=WMlz8wkBJuQTc7SmFbmIgoSh9u3CDpf0kn9K8mDM%2Buk%3D&os_level=23&os_id=cd30e294b997b28e&resolution=1080_1920&dpi=480&client_ip=192.168.1.100&pdunid=95AQACQTK6QEH'
        self.picture_id = []  # 存放图片的id
        self.picture_name = []  # 存放图片的名称
        self.picture_url = []  # 存放图片的url
        self.num = 0  # 得到的英雄的数目

    def get_picture_info(self):
        req = requests.get(self.target)
        html = json.loads(req.text)
        pic_info = html['list']
        self.num = len(pic_info)  # 得到元组的长度
        for each in pic_info:
            self.picture_name.append(each['name'])
            self.picture_id.append(each['hero_id'])
            self.picture_url.append(each['cover'])

    def downloader_picture(self):
        if os.path.exists('picture'):
            pass
        else:
            os.mkdir('picture')
        print('总共有%d个英雄'%self.num)
        for i in range(self.num):
            print('正在下载%s...'%self.picture_name[i])
            with closing(requests.get(url=str(self.picture_url[i])))as p:
                with open(r'picture\%s.jpg'%self.picture_name[i],'ab+') as f:
                    for chunk in p.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            f.flush()
                print('%s下载完成...'%self.picture_name[i])
        print('\n\n所有英雄下载完成！！！')

if __name__ == '__main__':
    gl = Downloader_picture()
    gl.get_picture_info()
    gl.downloader_picture()
