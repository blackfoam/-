#第一周第14课时 关于获取网页中的动态数据，异步加载

from bs4 import BeautifulSoup
import requests
import time

url ='https://www.knewone.com/discover?page=' ##discover 找不出来

def get_data(url,data=None):

    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    imgs = soup.select('a.cover-inner > img')
    titles = soup.select('article > section > h4 > a')
    links = soup.select('article > section > h4 > a')

    if data ==None:    #此处注意是== 不是=
        for img,title,link in zip(imgs,titles,links):
            data = {
                'img': img.get('src'), #是 src 记牢了
                'title':title.get('title'),
                'link':link.get('href')  #这个href咋来的不知道
            }
            print(data)
def get_more_page(start,end):
    for one in range(start,end):
        get_data(url+str(one))
        time.sleep(2)

get_more_page(1,10)

get_lin=[]
get_lin.append()