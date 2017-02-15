#第一周第12课时作业
from bs4 import BeautifulSoup
import requests
import time

def get_links(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        href = link.get('href')
        get_details(href)

def if_sex(sex_name):


    if sex_name == ['member_ico']:
        return '男'
    elif sex_name == ['member_ico1']:
        return '女'
    else:
        return '不明'

def get_details(url):
    wb_data=requests.get(url)
    soup= BeautifulSoup(wb_data.text,'lxml')
    #标题 地址 日租金 第一张房源图片链接 房东图片链接 房东性别 房东姓名
    titles=soup.select(' div.con_l > div.pho_info > h4 > em')
    addresss = soup.select('div.con_l > div.pho_info > p > span')
    rents = soup.select('div.day_l > span')
    imgs=soup.select('img[id="curBigImage"]')
    imjs=soup.select('div.member_pic > a > img')
    sexs = soup.select('div.member_pic > div')
    names=soup.select('div.w_240 > h6 > a')


    for img,imj,rent,address,title,sex,name in zip(imgs,imjs,rents,addresss,titles,sexs,names):#zip函数需加强, 此处必须一一对应卧槽
        data={
            'title':title.get_text(),
            'address':address.get_text().rstrip(),
            'rent':rent.get_text(),
            'img':img.get("src"),
            'imj':imj.get("src"),
            'sex':if_sex(sex.get('class'))
        }
        print(data)
urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14)]#这个函数不是很会
for url in urls:
    get_links(url)
    time.sleep(4)