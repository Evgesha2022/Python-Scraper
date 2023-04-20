import json


class Result:

    def __init__(self, path):
        self.path = path

    @property
    def get_data(self):
        with open(self.path, 'r', encoding='utf-8') as f:
            try:
                my_data = json.load(f) # parse the JSON with load()
                return my_data
            except BaseException as e:
                print('The file contains invalid JSON')
                return []
    @property
    def change_data(self):
        ls = {}
        for key, item in self.get_data.items():
            nls = {}
            for k, v in item.items():
                percent = (v / item["Всего"]) * 100 if item["Всего"] != 0 else 0
                nls[k] = round(percent, 2)
            ls[key] = nls
        
        return ls
    def save(self, json_file_path):
        ds = json.dumps(self.change_data, indent=4, ensure_ascii=False)
        
        file = open(json_file_path, "w")
        file.write(ds)




