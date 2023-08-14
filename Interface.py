import Note
import os

def user_menu():
    print("\n Приветствуем вас в приложении \'Заметки\'! Выберите действие:  "
          "\n 1 - Сделать новую заметку"
          "\n 2 - Редактировать заметку"
          "\n 3 - Удалить заметку"
          "\n 4 - Показать все заметки"
          "\n 5 - Показать заметку от определенной даты"
          "\n 6 - Выйти"
          "\n Введите номер действия:  ")
    
def create_new_note(num):
    title = min_text_length(
        input('Введите название заметки: '), num)
    body = min_text_length(
        input('Введите описание заметки: '), num)
    return Note.Note(title = title, body = body)

def min_text_length(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов.\n')
        text = input('Введите текст: ')
    else:
        return text