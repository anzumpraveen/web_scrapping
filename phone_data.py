import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint


def get_data():
    dict={}
    p = requests.get("https://www.oppo.com/en/smartphones/series-find-x/find-x3-pro/#camera-sections")
    s = BeautifulSoup(p.text,"html.parser")
    camera=s.find("div",class_="camera-specs-text ultra-wide").get_text().strip()[:28]
    colour=s.find("div",class_="row-2").get_text()
    name=s.find("li",class_="selected").get_text()
    # print(name)

    dict["Phone_name"]=name
    dict["Camera"]=camera
    dict["Color"]=colour
    pprint(dict)

    with open("phone_information.json","w+") as phone_data:
        json.dump(dict,phone_data,indent=4)

get_data()