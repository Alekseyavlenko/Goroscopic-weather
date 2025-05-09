import sqlite3


def check_user_info(username, password):
    # есть ли пользователь с таким юзернэймом и совпадает ли пароль
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        #  не найден
        return False
    stored_password = row[0]
    return stored_password == password
