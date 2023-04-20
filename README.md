# Python-Scraper
Parsing the site https://www.sostav.ru/ratings/business to calculate how much money was spent on each category of advertising, the data output format json.
Before running the code, you should install the libraries.
```python
import requests
import bs4
```

In the download.py file, download the html page https://www.sostav.ru/ratings/business for further scraper.
```python
r = requests.get(self.url)
        html = r.text
```
In the parser.py file, we parse our downloaded page and issue data in json format for further work with them. Generates a tree parse for the parsed pages, allowing data from HTML to be used.
```python
 with open(self.source) as fp:
            soup = BeautifulSoup(fp, 'html.parser')
            return soup
```
In the data.py file, we process the data by calculating the percentage spent on each section. 
``` python
ls = {}
        for key, item in self.get_data.items():
            nls = {}
            for k, v in item.items():
                percent = (v / item["Всего"]) * 100 if item["Всего"] != 0 else 0
                nls[k] = round(percent, 2)
            ls[key] = nls
```
In the init.py file, we group everything together and run it to test the code.
