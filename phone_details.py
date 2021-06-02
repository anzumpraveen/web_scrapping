import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint

page = requests.get("https://www.oppo.com/en/smartphones/")
soup = BeautifulSoup(page.text,"html.parser")

def scrap_detail_phone():
    data={}
    div=soup.find("div","swiper-slide active")
    div1=div.find_all("div",class_="description")
    link=[]
    name_=[]
    for i in div1:
        url=i.find("a").get("href")
        link.append(url)
        phone_name=i.find("a").get_text().strip()
        name_.append(phone_name)

    index=0
    link_list=[]
    while index<len(link):
        data[name_[index]]=[link[index]]
        dict1=data
        index+=1
    pprint(data)
    with open("phone_quarys.json","w+")as json_data:
        json.dump(data,json_data,indent=4)

scrap_detail_phone()
