from Viever import Viever
from Notes_list import Notes_list
from Saver import Saver
from Opener import Opener


class Presenter:
    filter_notes = False
    filter_year = 0

    def __init__(self, notes_list: Notes_list, viever: Viever, saver: Saver, opener: Opener):
        self.notes_list = notes_list
        self.viever = viever
        self.saver = saver
        self.opener = opener

    def run(self):
        self.notes_list.list_notes = self.opener.open_json()
        while True:
            self.saver.save_json(self.notes_list)
            if self.filter_notes == False:
                self.viever.viev_notes_list(self.notes_list)
            else:
                self.viever.filter_viev_notes_list(
                    self.notes_list, self.filter_year)
            number = self.viever.menu()
            # Добавление заметки
            if number == 1:
                title = self.viever.menu_add_notes_title()
                body = self.viever.menu_add_notes_body()
                self.notes_list.add_notes(title, body)

            # Редактирование заметки
            if number == 2:
                temp = self.viever.menu_rewrite_notes(
                    self.notes_list.get_len())
                if temp == 0:
                    pass
                else:
                    title = self.viever.menu_rewrite_notes_title()
                    body = self.viever.menu_rewrite_notes_body()
                    self.notes_list.rewrite_notes(temp, title, body)

            # Удаление заметки
            if number == 3:
                temp = self.viever.menu_rm_notes(self.notes_list.get_len())
                if temp == 0:
                    pass
                else:
                    self.notes_list.rm_notes(temp)

            # Фильтр по году
            if number == 4:
                temp = self.viever.filter_year_notes()
                if temp == 0:
                    self.filter_notes = False
                else:
                    self.filter_year = temp
                    self.filter_notes = True

            # Выход
            if number == 5:
                return 0
