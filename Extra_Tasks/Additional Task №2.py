def standartize_name(name: str) -> str:
    '''
    Стандартизирует имя контакта
    name - имя контакта
    '''
    return name.title()

def standartize_phone(phone: str) -> str:
    '''
    Стандатизирует номер телефона
    phone - номер телефона
    '''
    phone_digits = ''.join(char for char in phone if char.isdigit())
    if len(phone_digits) == 10:
        return '+7' + phone_digits
    elif len(phone_digits) == 11:
        return '+7' + phone_digits[1:]
    else:
        return phone_digits
    
def add_contact(phone_book:dict) -> dict:
    '''
    Добавляет контакт в телефонную книгу
    phone_book - телефонная книга
    '''
    name = input("Введите имя контакта: ")
    phone = input("Введите номер телефона: ")

    standartized_name = standartize_name(name)
    standartized_phone = standartize_phone(phone)

    new_phone_book = phone_book.copy()
    new_phone_book[standartized_name] = standartized_phone
    print("Контакт успешно добавлен!")
    return new_phone_book

def delete_contact(phone_book:dict) -> dict:
    '''
    Удаляет контакт из телефонной книги
    phone_book - телефонная книга
    '''
    name = input("Введите имя контакта: ")
    standartized_name = standartize_name(name)

    if standartized_name in phone_book:
        new_phone_book = phone_book.copy()
        del new_phone_book[standartized_name]
        print("Контакт успешно удалён!")
        return new_phone_book
    else:
        print("Контакт не найден!")
        return phone_book
    
def view_contact(phone_book:dict) -> dict:
    '''
    Просматривание телефонной книги
    phone book - телефонная книга
    '''
    if not phone_book:
        print("Телефоная книга пуста")
    else:
        for name, phone in phone_book.items():
            print(f"{name}: {phone}")

def edit_contact(phone_book:dict) -> dict:
    '''
    Изменение контаков в телефонной книге
    phone_book - телефонная книга
    '''
    name = input("Введите имя: ")
    standartized_name = standartize_name(name)

    if standartized_name in phone_book:
        new_phone = input("Введите новый номер телефона: ")
        standartized_phone = standartize_phone(new_phone)
        new_phone_book = phone_book.copy()
        new_phone_book[standartized_name] = standartized_phone
        return new_phone_book
        print("Номер телефона успешно изменён")
    else:
        print("Ошибка")
        return phone_book

def menu():
    '''
    Меню выбора 
    '''
    phone_book = {}
    while True:
        print("\n Выберите функцию:")
        print("1. Добавить контакт")
        print("2. Удалить контакт")
        print("3. Показать список контактов")
        print("4. Изменить номер")
        print("5. Выход")
 
        choice = input("Введите номер функции: ")

        if choice == '1':
            phone_book = add_contact(phone_book)
        elif choice == "2":
            phone_book = delete_contact(phone_book)
        elif choice == "3":
            view_contact(phone_book)
        elif choice == "4":
            phone_book = edit_contact(phone_book)
        elif choice == "5":
            print("Выход из программы")
            break
        else:
            print("Неверный выбор, выберите другой номер!")    
menu()
