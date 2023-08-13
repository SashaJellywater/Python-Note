import Interface
import function as f

user_choice = ''
while user_choice != '6':
        
        Interface.user_menu()
        user_choice = input().strip()

        if user_choice == '1':
             f.add_note()
        if user_choice == '2':
             f.show("all")
             f.id_show("edit")
        if user_choice == '3':
              f.show("all")
              f.id_show("del")
        if user_choice == '4':
              f.show("all")
        if user_choice == '5':
              f.show("date")
        if user_choice == '6':
            print("Всего доброго")
            break