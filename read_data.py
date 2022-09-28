import csv

table = ['last_name', 'name', 'phone_number', 'post', "salary"]


def find_data():
    request = input("Введите значение поиска: ")
    with open("data.csv", encoding="utf=8") as file:
        reader = csv.reader(file, delimiter=',')
        for line in reader:
            if request in line:
                description = dict(zip(table, line))
                for key, value in description.items():
                    print(f'{key}: {value}')

    return request