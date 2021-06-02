import requests
from bs4 import BeautifulSoup
import json
from pprint import pprint
page = requests.get("https://www.flipkart.com/apple-iphone-11-red-64-gb/p/itmc3935326f2feb?pid=MOBFWQ6BYYV3FCU7&lid=LSTMOBFWQ6BYYV3FCU7JCCDZJ&marketplace=FLIPKART&q=iphone+11&store=tyy%2F4io&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_6_na_na_na&fm=SEARCH&iid=650b9660-6749-4250-85eb-b450a2efa3c8.MOBFWQ6BYYV3FCU7.SEARCH&ppt=sp&ppn=sp&ssid=2jch47tjog0000001622171948056&qH=f6cdfdaa9f3c23f3")
soup = BeautifulSoup(page.text,"html.parser") 

def scrop_phone_data():
    dict={}
    name=soup.find("span",class_="B_NuCI").get_text()[:-12]
    colour=soup.find("span",class_="B_NuCI").get_text()[17:-8]
    ROM=soup.find("li",class_="_21Ahn-").get_text()
    rating=soup.find("div",class_="_3LWZlK").get_text()
    price=soup.find("div",class_="_30jeq3 _16Jk6d").get_text()[1:]
    display=soup.find("div",class_="_2418kt").get_text()[9:53]
    camera=soup.find("div",class_="_2418kt").get_text()[54:-22]
    chip=soup.find("div",class_="_2418kt").get_text()[-22:].strip()
    dict["Phone_name"]=name
    dict["Phone_ROM"]=ROM
    dict["Phone_rating"]=rating
    dict["Phone_price"]=price
    dict["Phone_display"]=display
    dict["Phone_camera"]=camera
    dict["Phone_chip"]=chip
    with open("details_iPhone11pro.json","w+")as json_detail:
        json.dump(dict,json_detail,indent=4)
scrop_phone_data()