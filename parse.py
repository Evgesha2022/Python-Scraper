import bs4
import re
import requests
from bs4 import BeautifulSoup
import json

from data import Result
from download import Downloader 




class Parser:
    def __init__(self, source):  #это должен быть web_page
        self.source = source
        
    @property
    def parse(self):
        dl = len(self.soup.find_all("table", attrs={"class": "r-table"}))
        
        table = self.soup.find_all("table", attrs={"class": "r-table"})[0]
        
        headers = []
        for i in table.find_all('th')[2:]:# здесь заголовки интернет пресса и тд
            title = i.text
            headers.append(title)
        

        mydata ={}
        names =[]

        for j in table.find_all('tr')[1:]:#здесь появляются имена сбер и тд
            for i in j.find_all('td')[1:2]:    
                names.append(i.text)
        in_data={}
        d=0
        for j in table.find_all('tr')[1:]:
            k=0
            for i in j.find_all('td')[2:]:  #в этом блоке надо форматировать данные
                if i.text == '-':
                    in_data[headers[k]] = 0
                else:
                    try:
                        in_data[headers[k]] = int(i.text.replace(' ', ''))
                    except ValueError as e:
                        in_data[headers[k]] = float(i.text.replace(',', '.'))    
                k += 1
            mydata[names[d]]=in_data
            in_data={}
            d+=1 
        return mydata
    
    @property
    def soup(self):
        with open(self.source) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            return soup
    def save(self, json_file_path):
        ds = json.dumps(self.parse, indent=4, ensure_ascii=False)
        
        file = open(json_file_path, "w")
        file.write(ds)

web_page = "test.html" 
parsed_web_page = "data.json"
parser = Parser(web_page)

parser.save(parsed_web_page)

