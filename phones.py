from csv import DictReader, DictWriter
from os.path import exists
file_name = "phone.csv"


def get_info():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = 98767576987
    flag = False
    while not flag:
        try:
            phone_number = int(input("Введите номер телефона: "))
            if len(str(phone_number)) != 11:
                print("Неверная длина номера")
            else:
                flag = True
        except ValueError:
            print("Некорректный номер")
    return [first_name, last_name, phone_number]


def create_file(file_name):
    with open(file_name, "w", encoding="utf-8", newline='') as data:
        f_w = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_w.writeheader()


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as data:
        f_r = DictReader(data)
        return list(f_r)


def write_file(file_name, lst):
    res = read_file(file_name)
    obj = {"Имя": lst[0], "Фамилия": lst[1], "Телефон": lst[2]}
    res.append(obj)
    with open(file_name, "w", encoding="utf-8", newline='') as data:
        f_w = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_w.writeheader()
        f_w.writerows(res)


def copy_number(file_name, row):
    res = read_file(file_name)
    res_copy = read_file("copy_" + file_name)
    res_copy.append(res[row-1])
    with open("copy_" + file_name, "w", encoding="utf-8", newline='') as data:
        f_w = DictWriter(data, fieldnames=["Имя", "Фамилия", "Телефон"])
        f_w.writeheader()
        f_w.writerows(res_copy)


def main():
    while True:
        command = input("Введете команду: ")
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name, get_info())
        elif command == 'r':
            if not exists(file_name):
                print("Файл отсутствует, создайте его")
                continue
            print(*read_file(file_name), sep="\n")
        elif command == 'c':
            print(*read_file(file_name), sep="\n")
            row = int(input("Введите номер строки для копирования: "))
            copy_number(file_name, row)


print("Команды:", "w - записать новые данные", "r - открыть файл",
      "c - копировать данные в другой файл", "q - выход", sep="\n")
main()
