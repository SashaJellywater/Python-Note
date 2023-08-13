import Interface
import function as f

user_choice = ''
while user_choice != '6':
        Interface.menu()
        user_choice = input().strip()
        if user_choice == '1':
             f.add_note()

        if user_choice == '6':
            print("Всего доброго")
            break