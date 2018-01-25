import requests
from bs4 import BeautifulSoup


class downloader(object):
    def __init__(self):
        self.target = "http://www.biqukan.com/17_17851/"  # 小说的章节地址
        self.server = "http://www.biqukan.com"
        self.names = []  # 章节名称
        self.urls = []  # 章节路径
        self.nums = 0  # 章节数目

    '''得到章节名称'''

    def get_chapter_url(self):
        # 得到网页源码信息
        html = requests.get(url=self.target)
        # 将网络源码信息规范化
        div_bf = BeautifulSoup(html.text, "lxml")
        # 查找第一层的目的内容
        bf = div_bf.find_all('div', class_='listmain')
        # 规范化
        a_bf = BeautifulSoup(str(bf), "lxml")
        # 查找含有a的内容
        a = a_bf.find_all('a')
        # 得到章节的数目
        self.nums = len(a[21:])
        for i in a[21:]:
            # 将得到的路径存放到元组urls[]
            self.urls.append(i.get('href'))
            # 将得到的章节题目存放到names[]
            self.names.append(i.string)

        '''
        函数说明:得到每一章节的内容
        parameters:
            target:self.urls[]中的每一章节的url
        return:
            paper:章节内容
        '''

    def get_chapter_contenter(self, target):
        # 得到每一章节的网页信息
        html = requests.get(url=(self.server + target))
        # 将得到的网页信息规范化
        paper_bf = BeautifulSoup(html.text, "lxml")
        # 查找并提取感兴趣的内容
        paper = paper_bf.find_all('div', class_='showtxt')
        paper = paper[0].text.replace('\xa0' * 8, '\n\n')
        return paper

    '''将得到内容存放到txt文件中'''

    def writer(self, filename, name, content):#文件名称，章节名称，章节内容
        with open(filename, 'a', encoding='utf-8') as f:
            #将章节名称写入，以回车结束
            f.write(name + '\n')
            #将章节内容写入，以两个回车结束
            f.writelines(content)
            f.write('\n\n')

if __name__=='__main__':
    dl = downloader()
    dl.get_chapter_url()
    for each in range(dl.nums):
        content=dl.get_chapter_contenter(dl.urls[each])
        dl.writer("寻师有计出师表.txt",dl.names[each],content)
        print(dl.names[each]+"......下载完成\n")