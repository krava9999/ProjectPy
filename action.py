import json


from datetime import datetime


def openJson():
    with open('notes.json', encoding='utf-8') as file:
        data = json.load(file)
        return data


# функция принимает аргумент. Если  0 - выводим все заметки, если что то другое, то выводим заметку по id.
def readNotes(variable):
    data = openJson()
    if variable == '0':
        for note in sorted(data['notes'], key=lambda x: x['dateTime']):
            print(
                f"Заментка №{note['id']}:\n Заголовок: {note['title']}\n Описание: {note['desc']}\n Дата и время создания: {note['dateTime']}\n")
    else:
        for note in data['notes']:
            if note['id'] == variable:
                print(
                    f"Заментка №{note['id']}:\n Заголовок: {note['title']}\n Описание: {note['desc']}\n Дата и время создания: {note['dateTime']}\n")


def addNote():
    data = openJson()
    id = str(len(data['notes'])+1)
    title = input('Введите заголовок: ')
    desc = input('Введите описание: ')
    dateTime = datetime.now().strftime('%d/%m/%y %H:%M')
    newNote = {
        "id": id,
        "title": title,
        "desc": desc,
        "dateTime": dateTime
    }
    data['notes'].append(newNote)
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)


def editNote():
    data = openJson()
    searchIdNote = input('Введите id заметки которую нужно отредактировать: ')
    for note in data['notes']:
        if note['id'] == searchIdNote:
            note['title'] = input('Введите заголовок: ')
            note['desc'] = input('Введите описание: ')
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)


def delNote():
    data = openJson()
    numNote = input('Введите номер заметки: ')
    for note in data['notes']:
        if note['id'] == numNote:
            data['notes'].remove(note)
    print(data['notes'])
    with open('notes.json', 'w', encoding='utf-8') as file:
        json.dump(data, file)
