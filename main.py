import action


while (True):
    act = input('''Введите номер действия:
    0 - Закончить работу
    1 - Вывести заметки
    2 - Добавить заметку
    3 - Редактировать заметку
    4 - Удалить заметку
--> ''')
    if act == '0':
        break
    elif act == '1':
        variable = input(
            "Введите номер заметки или введите 0 если хотите вывести все заметки: ")
        action.readNotes(variable)
    elif act == '2':
        action.addNote()
    elif act == '3':
        action.editNote()
    elif act == '4':
        action.delNote()
