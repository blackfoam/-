from bs4 import BeautifulSoup
import requests
import time

url = 'http://bj.58.com/pingbandiannao/24604629984324x.shtml'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')



def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml')
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    # 这个是找到了58的查询接口，不了解接口可以参照一下新浪微博接口的介绍
    js = requests.get(api)
    views = js.text.split('=')[-1]
    # return views
    print(views)

get_views_from(url)