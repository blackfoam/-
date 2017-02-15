#第一周大作业：爬取58同城的数据
from bs4 import BeautifulSoup
import requests
url= 'http://bj.58.com/pingbandiannao/26520838295997x.shtml' #网址的？不带

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')

def get_links_from(who_sells):
    urls = []
    list_view = 'http://bj.58.com/pbdn/{}/pn2/'.format(str(who_sells))#这里的网页是指产品所在的列表页
    wb_data = requests.get(list_view)#此处解析的网页要搞清楚，不是URL了
    soup = BeautifulSoup(wb_data.text,'lxml')
    for link in soup.select('td.t a.t'):
        urls.append(link.get('href').split('?')[0])
    return urls

def get_views_from(url):
    id = url.split('/')[-1].strip('x.shtml') #split的格式是这样（''）【】的
    api = 'http://jst1.58.com/counter?infoid={}'.format(id)
    js = requests.get(api) #请求网页用requests
    views = js.text.split('=')[-1] #text text text
    return views

def get_item_info(who_sells=0):
    urls=get_links_from(who_sells)
    for url in urls:

        wb_data=requests.get(url)
        soup = BeautifulSoup(wb_data.text,'lxml')
        data= {
            'title' : soup.title.text,
            'price' : soup.select('.price')[0].text,
            'area' : list(soup.select('.c_25d')[0].stripped_strings) if soup.find_all('span','c_25d') else None,
            'data' : soup.select('.time')[0].text,
            'cata' : '个人'if who_sells == 0 else'商家',
            'view': get_views_from(url)
        }
        print(data)

get_item_info(1)

#get_link_from(0)

#get_view_from(url)