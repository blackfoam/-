#Python实战计划学习笔记1-3：爬取租房信息
import requests
from bs4 import BeautifulSoup
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
        return '不明'   #爬取的时候发现有些房东没有填写性别，所以用了else。

def get_details(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')


    titles = soup.select('div.con_l > div.pho_info > h4 > em')
    addresss = soup.select('div.con_l > div.pho_info > p > span')
    prices = soup.select('div.day_l > span')
    images = soup.select('img[id="curBigImage"]')
    landlords = soup.select('div.member_pic > a > img')
    names = soup.select('div.w_240 > h6 > a')
    sexs = soup.select('div.member_pic > div')

    for title, address, price, image, landlord, name, sex in zip(titles, addresss, prices, images, landlords, names, sexs):
        data = {

            'title': title.get_text(),
            'address': address.get_text().rstrip(),
            'price': price.get_text(),
            'image': image.get("src"),
            'landlord': landlord.get("src"),
            'name': name.get_text(),
            'sex': if_sex(sex.get('class'))
        }
        print(data)

urls = ['http://bj.xiaozhu.com/search-duanzufang-p{}-0/'.format(str(i)) for i in range(1,14)]
for url in urls:
    get_links(url)
    time.sleep(4)