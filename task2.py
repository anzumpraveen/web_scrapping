import requests
import json
from bs4 import BeautifulSoup
# from task1 import scrap_top_list
# movies = scrap_top_list()
file1 = open("saral_task1.json")
movies = json.load(file1)
def group_by_year():
    # main_list=[]
    emp_dic={}
    for i in movies:
        movie_list=[]
        for j in movies:
            if i["Year"]==j["Year"]:
                movie_list.append(i)
                emp_dic[i["Year"]]=movie_list
        # main_list.append(emp_dic)
        

    with open("saral_task2.json","w+")as file:
        json.dump(emp_dic,file,indent=4)
        a=json.dumps(emp_dic)

group_by_year()
