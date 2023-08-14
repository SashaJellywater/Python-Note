import Note
import operation
import Interface

min_num = 2

def add():
    note = Interface.create_new_note(min_num)
    array = operation.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    operation.write_file(array, 'a')
    print("Заметка добавлена!")

def show(text):
    array = operation.read_file()
    if text=="date":
        date = input("Введите дату в формате dd.mm.yyyy: ")
    for notes in array:
        count = 0
        if text == "all":
            print(Note.Note.print_note(notes))
        if text == "date":
            if date in Note.Note.get_date(notes):
                print(Note.Note.print_note(notes))
            else: count = 1
    if count == 1:
        print(f"Заметки с датой {date} не найдены.")

def id_show(text):
    id = input("Введите ID необходимой заметки: ")
    array = operation.read_file()
    count = 0
    for notes in array:
        if id == Note.Note.get_id(notes):
            count = 1
            if text == "edit":
                note = Interface.create_new_note(min_num)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print(f"Заметка изменена.")
            if text == "del":
                array.remove(notes)
                print(f"Заметка удалена.")
    if count == 0:
        print("Такой заметки нет, возможно, вы ввели неверный ID")
    operation.write_file(array, 'a')