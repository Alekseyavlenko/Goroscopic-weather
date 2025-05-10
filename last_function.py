import csv


def check_user_horoscope(username, password):
    try:
        with open('data/users.csv', encoding='utf-8') as users_file:
            reader = csv.reader(users_file, delimiter=';', quotechar='"')
            next(reader)
            for row in reader:
                if row[1] == username and row[2] == password:
                    return bool(int(row[3]))
        return None  # пользователь не найден
    except FileNotFoundError:
        return None  # файл не найден


