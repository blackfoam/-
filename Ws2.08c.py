##这是照着视频敲了一遍，构造函数其实不大明白
from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent': '',
    'Cookie': ''
}

url_saves = 'http://www.tripadvisor.com/Saves#37685322'
url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'

def get_attractions(url,data=None):
    wb_data= requests.get(url)
    soup= BeautifulSoup(wb_data.text,'lxml')
    titles  =soup.select('')
    imgs    =soup.select('')
    catas   =soup.select('')
    for title,img,cate in zip(titles,imgs,cates):
        data= {
            'title' :title.get_text(),
            'img'   :img.get('src'),
            'cate'  :list(cate.stripped_strings),
            }
        print(data)


def get_favs(url,data=None):
    wb_data = requests.get(url,headers=headers)
    soup    =BeautifulSoup(wb_data.text,'lmxl')
    titles    = soup.select('a.location-name')
    imgs      = soup.select('div.photo > div.sizedThumb > img.photo_image')
    metas = soup.select('span.format_address')

    if data==None:
        for title,img,meta in zip(titles,imgs,metas):
            data = {
                'title': title.get_text(),
                'img': img.get('src'),
                'cate': list(mate.stripped_strings),
            }
            print(data)
