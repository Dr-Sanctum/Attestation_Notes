import datetime
import jsonpickle
from Notes import Notes


class Notes_list:
    list_notes = []
    id = 1

    def add_notes(self, title: str, body_notes: str):
        self.list_notes.append(
            Notes(self.id, title, body_notes, datetime.datetime.today()))
        self.id = self.id + 1

    def rm_notes(self, number: int):
        self.list_notes.pop(number - 1)
        for i in range(len(self.list_notes)):
            self.list_notes[i].id_notes = i + 1
        self.id = self.id - 1

    def rewrite_notes(self, number_notes: int, title: str, body_notes: str):
        self.list_notes.insert(number_notes,
                               Notes(self.id, title, body_notes, datetime.datetime.today()))

    def get_len(self):
        return len(self.list_notes)

    def __str__(self):
        result = ''
        for i in range(len(self.list_notes)):
            if i < len(self.list_notes) - 1:
                result += f'{self.list_notes[i]} \n'
            else:
                result += f'{self.list_notes[i]}'
        return result

    def toJSON(self):
        return jsonpickle.encode(self.list_notes)
