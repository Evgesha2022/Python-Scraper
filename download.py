import requests


class Downloader:
    def __init__(self, url):
        self.url = url

    @property
    def get_html(self):
        r = requests.get(self.url)  # url - ??????
        html = r.text
        return html

    def save(self, file):
        f = open(file, 'w')
        f.write(self.get_html)
        f.close()


url = "https://www.sostav.ru/ratings/business"
new = Downloader(url)
path = "test.html"
new.save(path)
