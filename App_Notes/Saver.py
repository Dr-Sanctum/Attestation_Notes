import os
from Notes_list import Notes_list
class Saver:
    def save_json(self,data: Notes_list):
        with open(os.path.dirname(os.path.abspath(__file__)) +"\\data_file.json", 'w', encoding='utf-8') as write_file:
            write_file.write(data.toJSON())