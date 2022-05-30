<<<<<<< HEAD
import requests


url='https://www.douban.com//tag/小说'#目标网站
headers={'Referer': 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


wz=requests.get(url,headers)
print(wz.encoding)
html=wz.text
0print(html)
status=wz.status_code
=======
import requests


url='https://www.douban.com//tag/小说'#目标网站
headers={'Referer': 'https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}


wz=requests.get(url,headers)
print(wz.encoding)
html=wz.text
0print(html)
status=wz.status_code
>>>>>>> 35f57f95c4da97910439671ecc8f9845640829d6
print(status)