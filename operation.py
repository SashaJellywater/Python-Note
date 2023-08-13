import Note

def write_file(array, mode):
    notesFile = open("notes.csv", mode = "w", encoding='utf -8')
    notesFile.seek()
    notesFile.close()
    notesFile = open("notes.csv", mode=mode, encoding='utf - 8')
    for notes in array:
        notesFile.write(Note.Note.to_string(notes))
        notesFile.write("\n")
    notesFile.close

def read_file():
    try:
        array = []
        notesFile = open("notes.csv", "r", encoding='utf - 8')
        notes= notesFile.read().strip().split("\n")
        for n in notes:
            split = n.split(';')
            note = Note.Note(id = split[0], title = split[1], body = split[2], date = split[3])
            array.append(note)
    except Exception:
        print("Заметки не найдены")
    finally:
        return array
