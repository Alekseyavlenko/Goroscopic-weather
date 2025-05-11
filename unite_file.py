import csv
import os
import random
import sqlite3


# ----------------------------
# функция из presckazaniye.py
# ----------------------------

def get_random_prediction(zodiac_sign):
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    cursor.execute('SELECT prediction FROM predictions WHERE zodiac_sign = ?', (zodiac_sign,))
    predictions = cursor.fetchall()
    conn.close()
    if predictions:
        return random.choice(predictions)[0]
    else:
        return None


# ----------------------------
# функции из registration.py
# ----------------------------

def get_next_id():
    if not os.path.exists('data/users.csv'):
        return 0
    with open('data/users.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        return sum(1 for _ in reader) - 1


# ----------------------------
# функции из registr.py
# ----------------------------


def save_user_sqlite(username, password, wants_horoscope):
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (username, password, wants_horoscope) VALUES (?, ?, ?)',
            (username, password, wants_horoscope)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        return False
    conn.close()
    return True


# ----------------------------
# код из goroscop.py
# ----------------------------


if __name__ == '__main__':
    pass
