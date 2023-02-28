# #Задание
# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания
# или последнего изменения заметки. Сохранение заметок необходимо сделать
# в формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее.
# При чтении списка заметок реализовать фильтрацию по дате.

from Notes_list import Notes_list
from Viever import Viever
from Presenter import Presenter
from Opener import Opener
from Saver import Saver

new_viewer = Viever()
new_notes_list = Notes_list()
new_saver = Saver()
new_opener = Opener()
# new_notes_list.list_notes.append(Notes (1,"Мой дом","Улица Сосновая Дом 6", datetime.datetime(2005, 3, 8, 12, 23)))
# new_notes_list.list_notes.append(Notes (2,"Мой телефон","12341", datetime.datetime(2015, 2, 4, 8, 12)))
# new_notes_list.list_notes.append(Notes (3,"Моя машина","Ауди", datetime.datetime(2016, 1, 22, 3, 5)))

new_presenter = Presenter(new_notes_list, new_viewer, new_saver, new_opener)
new_presenter.run()
