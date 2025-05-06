import sqlite3


def init_db():
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            wants_horoscope INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


def save_user(username, password, wants_horoscope):
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    try:
        cursor.execute(
            'INSERT INTO users (username, password, wants_horoscope) VALUES (?, ?, ?)',
            (username, password, wants_horoscope)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True


if __name__ == '__main__':
    init_db()
    save_user("marktest", "12345", 1)
