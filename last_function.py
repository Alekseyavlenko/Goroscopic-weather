import sqlite3


def check_user_horoscope(username, password):
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    cursor.execute(
        'SELECT wants_horoscope FROM users WHERE username = ? AND password = ?',
        (username, password))
    result = cursor.fetchone()
    conn.close()

    # если пользователь найден (не None)
    if result is not None:
        return bool(result[0])
    # если пользователь не найден (None)
    else:
        return None
