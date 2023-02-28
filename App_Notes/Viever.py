from Notes_list import Notes_list

class Viever:
    def viev_notes_list(self, notes_list: Notes_list):
        print('Список заметок:')
        print(notes_list)

    def filter_viev_notes_list(self, notes_list: Notes_list, year: int):
        print('Список заметок:')
        result = ''
        for i in range(len(notes_list.list_notes)):
            temp = notes_list.list_notes[i].date_last.year
            if i <= len(notes_list.list_notes) - 1 and temp == year:
                result += f'{notes_list.list_notes[i]} \n'
            
        print(result)

    def menu(self):
        while True:
            print('Меню: \n' +
                '1. Добавить замтку \n' +
                '2. Редактировать замтку \n' +
                '3. Удалить заметку \n' +
                '4. Фильтровать по дате \n' +
                '5. Выход')
            temp = input('Выберите пункт меню: ')
            if str.isdigit(temp) and (int(temp) > 0 and int(temp) <= 5):
                return int(temp)
            else:
                print('Неверный пункт меню')

    def menu_add_notes_title(self):
        return input('Введите заголовок заметки: ')

    def menu_add_notes_body(self):
        return input('Введите текст заметки: ')
    
    def menu_rewrite_notes_title(self):
        return input('Введите новый заголовок заметки: ')

    def menu_rewrite_notes_body(self):
        return input('Введите новый  текст заметки: ')

    def menu_rewrite_notes(self, len_list: int):
        while True:
            if len_list == 0:
                print('Нет заметок.')
                return 0
            temp = input('Выберите номер заметки для редактирования (0 - отмена): ')
            if str.isdigit(temp) and (int(temp) >= 0 and int(temp) <= len_list):
                return int(temp)
            else:
                print('Неверный номер заметки')

    def menu_rm_notes(self, len_list: int):
        while True:
            if len_list == 0:
                print('Нет заметок.')
                return 0
            temp = input('Выберите номер заметки для удаления (0 - отмена): ')
            if str.isdigit(temp) and (int(temp) >= 0 and int(temp) <= len_list):
                return int(temp)
            else:
                print('Неверный номер заметки')

    def filter_year_notes(self):
        while True:
            temp = input('Выберите год для вывода заметок (0 - выключить фильтр): ')
            if str.isdigit(temp) and (int(temp) >= 0 and int(temp) <= 2023):
                return int(temp)
            else:
                print('Некорректный ввод')
