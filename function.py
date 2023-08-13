import Note
import operation
import Interface

min_num = 2

def add_note():
    note = Interface.create_new_note(min_num)
    array = operation.read_file()
    for notes in array:
        if Note.Note.get_id(note)==Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    operation.write_file(array, 'a')
    print("Заметка добавлена!")

def show(text):
    