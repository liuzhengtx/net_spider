# -*- coding:utf-8 -*-
"""""""""
   File Name：     downloader_picture1
   Description :   下载http://unsplash.com里面的壁纸
   Author :       liuzhengtx
   date：          2018/1/19
"""""""""
import requests, json, time, sys
from contextlib import closing


class Downloader_picture(object):
    def __init__(self):
        self.pictures_id = []
        self.target = 'http://unsplash.com/napi/feeds/home'
        self.headers = {'authorization': 'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
        self.server = 'https://unsplash.com/photos/xxx/download?force=trues'

    def get_ids(self):
        # 通过抓包程序，得到请求的来源（target）,反爬虫采用的是authorization，
        # 另vrify=False,不进行认证
        req = requests.get(url=self.target, headers=self.headers, verify=False)
        # 将字符串转为字典
        html = json.loads(req.text)
        # 得到下一页的地址
        next_page = html['next_page']
        time.sleep(1)
        for each in html['photos']:
            # 将每一张图片的id放到pictures_id
            self.pictures_id.append(each['id'])
        # 得到五页网页的图片id
        for i in range(5):
            # 得到解析的网页信息
            req = requests.get(url=next_page, headers=self.headers, verify=False)
            # 转化为字典形式
            html = json.loads(req.text)
            next_page = html['next_page']
            for each in html['photos']:
                self.pictures_id.append(each['id'])
            time.sleep(1)

    def downloader_picture(self, picture_id, filename):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        self.server = self.server.replace('xxx', picture_id)
        # 将字节以控制流的形式传入到r
        with closing(requests.get(url=self.server, headers=headers, stream=True, verify=False)) as r:
            # 新建空白的jpg文件
            with open('%d.jpg' % filename, 'ab+') as f:
                # 每次写入的最大字节的长度为1024
                for chunk in r.iter_content(chunk_size=1024):
                    # 判断是否写入完成
                    if chunk:
                        f.write(chunk)
                        # 刷新缓存
                        f.flush()


if __name__ == '__main__':
    gl = Downloader_picture()
    print('正在获取图片id...')
    gl.get_ids()
    print('图片id信息获取成功')
    for i in range(len(gl.pictures_id)):
        print('正在下载第%d张图片' % (i + 1))
        gl.downloader_picture(gl.pictures_id[i], (i + 1))
