if __name__ == "__main__":
    from download import Downloader
    from parse import Parser
    from data import Result
else:
    from .download import Downloader
    from .parse import Parser
    from .data import Result

url = "https://www.sostav.ru/ratings/business"
def process(url, path="test.html", data_path=None):

    #download
    new = Downloader(url)
    new.save(path)
    #parser
    web_page = "test.html" 
    parsed_data = "data.json"
    parser = Parser(path)
    parser.save(parsed_data)
    #data
    data = Result(parsed_data)
    path_ch = "changedata.json"
    data.save(path_ch)

process(url)

