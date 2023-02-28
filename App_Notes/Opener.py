import os
import jsonpickle
class Opener:
    def open_json(self):
        with open(os.path.dirname(os.path.abspath(__file__)) + "\\data_file.json", 'r', encoding='utf-8') as read_file:
            return jsonpickle.decode(read_file.read())