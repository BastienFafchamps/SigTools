import os
from glob import glob
import json

dir_path = os.path.dirname(os.path.realpath(__file__))
data_path = os.path.join(dir_path, 'data')

class Data():

    def __init__(self, modName):
        self.items = []
        self.items_names = []
        self.modName = modName

    def __get_folder_path(self, type):
        return os.path.join(data_path, self.modName, type)

    def __rchop(self, s, suffix):
        if suffix and s.endswith(suffix):
            return s[:-len(suffix)]
        return s

    def load_items(self):
        path = os.path.join(self.__get_folder_path('items'), '*.json')
        self.items = []
        for file_name in glob(path):
            try:
                with open(file_name, 'r') as json_file:
                    text = json_file.read()
                    name = self.__rchop(os.path.basename(file_name), '.json')

                    self.items.append({
                        'raw_text': text,
                        'data': json.loads(text),
                        'name': name,
                        'path': file_name
                    })
            except IOError:
                print(f'Could not read file: "{file_name}"')
        return self.items

    def set_item(self, path, text_value):
        if (os.path.isfile(path)):
            try:
                with open(path, 'w') as file:
                    file.write(text_value)
            except IOError:
                print(f'Could not write to file: "{path}"')