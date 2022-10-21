import csv
from csv import writer


def delete():
    request = input("Введите данные для удаления: ")

    with open('data.csv', 'r+') as in_f:
        data = list(csv.reader(in_f))
        in_f.truncate(0)

    data = list(filter(None, data))
    print(data)

    with open('data.csv', 'w', newline='') as out_f:
        for row in data:
            if request not in row:
                writer(out_f).writerow(row)
                print(row)

    return request
