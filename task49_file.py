# Задача №49. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


def add_contact(f):
    input_name = input('Ввендите имя: ')
    input_last_name = input('Введите фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Recording \n{data} added')


def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)


def search_contact(f):
    last_name = input('Введите имя ')
    adr_book = read_all(f)
    for line in adr_book:
        if last_name in line:
            print(line)


def delete_contact(f):
    surname_to_delete = input('Введите фамилию: ')
    name_to_delete = input('Введите имя: ')
    data = read_all(f)
    new_data = []
    for item in data:
        if surname_to_delete in item and name_to_delete in item:
            continue
        new_data.append(item)
    with open(f, 'w', encoding='utf-8') as fd: 
        fd.write(''.join(new_data))


def main():
    file = 'file.txt'
    while True:
        user_choice = input('1 - добавить запись;\n2 - прочитать всю тел. книгу;\n'
                            '3 - найти запись;\n4 - удалить запись;\nв - выход;\n Введите команду: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            delete_contact(file)
        elif user_choice == 'в':
            break


if __name__ == '__main__':
    main()
