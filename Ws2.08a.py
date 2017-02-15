#第一周的第12课时真实世界的网页解析
from bs4 import BeautifulSoup
import  requests

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text,'lxml')
#titles = soup.select('div.property_title > a[target="_blank"]')#怎么找出来的不知，copy select错误
imgs = soup.select('img[width="200"]')
cates = soup.select('div.p13n_reasoning_v2')#怎么找的也是不知道

for title,img,cate in zip(titles,imgs,cates):
     data = {
         'title':title.get_text(),
         'img':img.get('src'),
         'cate':list(cate.stripped_strings),
     }
     print(data)