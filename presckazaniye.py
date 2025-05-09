import random
import sqlite3


def get_random_prediction(zodiac_sign):
    conn = sqlite3.connect('goroscope.db')
    cursor = conn.cursor()
    cursor.execute('SELECT prediction FROM predictions WHERE zodiac_sign = ?', (zodiac_sign,))
    predictions = cursor.fetchall()
    conn.close()
    if predictions:
        return random.choice(predictions)[0]
    else:
        return


