import time 
from lxml import etree
import requests




#url='https://pic.netbian.com/4kyouxi/index'
h={'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3875.400 QQBrowser/10.8.4492.400'}

urls=['https://pic.netbian.com/4kyouxi/index.html']
#https://pic.netbian.com/4kyouxi/index_2.html
data=[]
datalist=[]

page=int(input('爬取页数：'))
for n in range(1,page):
    url='https://pic.netbian.com/4kyouxi/index'
    url=url+str('_')+str(n+1)+str('.html')
    urls.append(url)

    url='https://pic.netbian.com/4kyouxi/index'
#print(urls)



for url in urls:
    html=requests.get(url,headers=h).text
    html=etree.HTML(html)
    result=etree.tostring(html,encoding="utf-8",pretty_print=True,method="html")
    urlall=html.xpath('//div[@class="slist"]/ul/li')#//*[@id="main"]/div[3]/ul
    print(urlall)


        
    for x in urlall:
        #//*[@id="main"]/div[3]/ul/li[1]从此开始
        url_title=x.xpath('./a/img/@src')#//*[@id="main"]/div[3]/ul/li[1]/a/b   #//*[@id="main"]/div[3]/ul/li[1]/a/img
        print(url_title)
        title=x.xpath('./a/b/text()')
        print(title)
        print('\n')

        