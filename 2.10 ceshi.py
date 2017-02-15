from bs4 import BeautifulSoup
import requests
import time


url ='https://knewone.com/?page=4'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
imgs = soup.select('a.cover-inner > img')
print(imgs)
titles = soup.select('article > section > h4 > a')
links = soup.select('article > section > h4 > a')

for img,title,link in zip(imgs,titles,links):
    data = {
        'img': img.get('src'),
        'title':title.get('title'),
        'link':link.get('href')  #这个href咋来的不知道
    }
    print(data)