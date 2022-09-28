import csv
from csv import writer


def delete():
    request = input("Введите данные для удаления: ")
    
    with open('data.csv', 'r') as inp:
        newrows = []
        data = csv.reader(inp)
        for row in data:
            if request not in row:
                newrows.append(row)
    with open('data.csv', 'w') as out:
        csv_writer = writer(out)
        for row in newrows:
            csv_writer.writerow(row)
        print(f' Строка с значением {request} удалена')


    return request