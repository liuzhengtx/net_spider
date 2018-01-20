#-*- coding:UTF-8 -*-
import requests,re, json
from bs4 import BeautifulSoup

class video_downloader():
    def __init__(self, url):
        self.server = 'http://api.xfsub.com'
        self.api = 'http://api.xfsub.com/index.php?url='
        self.get_url_api = 'http: // api.xfsub.com / xfsub_api / url.php'
        self.url = url.split('#')[0]
        self.target = self.api + self.url
        self.s = requests.session()

    """
    函数说明:获取key、time、url等参数
    Parameters:
        无
    Returns:
        无
    Modify:
        2017-09-18
    """
    def get_key(self):
        req=requests.session().get(url=self.target)
        print(req.text)
        req.encoding = 'utf-8'
        # self.info = json.loads(re.findall('"url.php",\ (.+),', req.text)[0])    #使用正则表达式匹配结果，将匹配的结果存入info变量中

if __name__ == '__main__':
     url = 'http://v.youku.com/v_show/id_XMTUzMjI2OTE0NA==.html?spm=a2hmv.20009921.yk-slide-86993.5~5~5~5!2~A'
     vd = video_downloader(url)
     vd.get_key()