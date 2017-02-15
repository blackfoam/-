#根据1周十四课时的作业
# unknown url type: '//wx4.sinaimg.cn/mw600/c0788b86ly1fckjivlvc4j20ku0uuadh.jpg' 总是编译不成功，不知为何。
from bs4 import BeautifulSoup
import requests,urllib.request
#记得header后面跟字典
header={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36','Cookie':'jdna = 01b0531fab6a989460dd1b231010b496  #1486821520944; Hm_lvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1486818727; Hm_lpvt_fd93b7fb546adcfbcf80c4fc2b54da2c=1486821522; _ga=GA1.2.1603557999.1486818728; _gat=1'}
url= 'http://www.jandan.net/ooxx/page-2346'
wb_data=requests.get(url,headers=header)
data_text=wb_data.text

soup=BeautifulSoup(data_text)

download_link=[]
file_path='/Users/wangzi/b3/'
for get_pic in soup.find_all('img'):
    pic_link=get_pic.get('src')
    download_link.append(pic_link)

for item in download_link:
    urllib.request.urlretrieve(item,file_path + item[-10:])
    print('done')