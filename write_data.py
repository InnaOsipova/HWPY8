import csv

table = ['last_name', 'name', 'phone_number', 'post', "salary"]


def get_data():
    choise = input ('Выберите список ввода 1 - однострочный, 2 - многострочный : ')
    if choise == '1':
        print ('Введите фамилию, имя, номер телефона, должность, заработную плату через запятую в одну строку :')
        record = input().split(',')
        print(record)
    elif choise == '2':
        record = [input(f'{i} :') for i in table]
    with open('data.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(record)

    print("Данные успешно записаны")
    return record