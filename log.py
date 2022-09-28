from datetime import datetime


def write_log(data, mode):
    if mode == "w":
        edit_log(f'Запись данных в {datetime.now()} : {data}\n')
    if mode == "d":
        edit_log(f'Удаление данных в {datetime.now()} : {data}\n')
    else:
        edit_log(f'Поиск данных {datetime.now()} : {data}\n')


def edit_log(text):
    with open("log.txt", "a", encoding="utf-8") as file:
        file.write(text)