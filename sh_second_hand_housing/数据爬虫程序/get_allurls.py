#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import requests
from bs4 import BeautifulSoup


# In[6]:


#生成需要爬取的页数的url
def generate_allurl(user_in_number):
    urls_outer=[]
    for url_next in range(1,user_in_number+1):
        url='https://sh.lianjia.com/ershoufang/pg{}/'
        url=url.format(url_next)
        urls_outer.append(url)
    return(urls_outer)
    
         #获取每一页的房源url链接汇总
def get_allurl():
    urls_inner=[]
    user_in_number=int(input('请输入生成页数：'))
    for url in generate_allurl(user_in_number):
        get_url = requests.get(url)
        if get_url.status_code == 200:
            re_set = re.compile('https://sh.lianjia.com/ershoufang/[0-9]+\.html')
            re_get = re.findall(re_set,get_url.text)#返回列表值
            re_get=list(set(re_get))#去除重复项目
            urls_inner.append(re_get)#返回嵌套列表
    allurls=[i for k in urls_inner for i in k]#将嵌套列表展开
    return(allurls)

