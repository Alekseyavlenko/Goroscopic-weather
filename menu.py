import sqlite3
import tkinter as tk
from tkinter import messagebox

DB_NAME = 'users.db'


# Создаем/подключаемся к базе и создаем таблицу
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            horoscope INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Добавление пользователя
def add_user(username, password, horoscope):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO users (username, password, horoscope) VALUES (?, ?, ?)',
                       (username, password, int(horoscope)))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False  # пользователь уже существует
    finally:
        conn.close()


# Проверка пользователя при входе
def check_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    conn.close()
    if row and row[0] == password:
        return True
    return False


# Получить настройки пользователя
def get_user_settings(username):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT horoscope FROM users WHERE username = ?', (username,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return bool(row[0])
    return False


# Обновить настройки пользователя
def update_user_settings(username, horoscope):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('UPDATE users SET horoscope = ? WHERE username = ?', (int(horoscope), username))
    conn.commit()
    conn.close()


class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Прогноз погоды - Меню')
        self.current_user = None
        self.bg_color = 'beige'  # Цвет фона по умолчанию
        self.root.configure(bg=self.bg_color)
        self.center_window()
        self.create_main_menu()

    def center_window(self):
        width = 1200
        height = 800

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_main_menu(self):
        self.clear_window()
        self.root.configure(bg=self.bg_color)

        tk.Label(self.root, text='Главное меню', font=('Arial', 24), bg=self.bg_color).pack(pady=20)

        tk.Button(self.root, text='Регистрация', width=20, height=2, font=('Arial', 16), command=self.register_window,
                  bg=self.bg_color).pack(pady=10)
        tk.Button(self.root, text='Вход', width=20, height=2, font=('Arial', 16), command=self.login_window,
                  bg=self.bg_color).pack(pady=10)
        tk.Button(self.root, text='Выход', width=20, height=2, font=('Arial', 16), command=self.root.quit,
                  bg=self.bg_color).pack(pady=10)
        self.create_color_menu()

    def create_color_menu(self):
        color_menu = tk.Frame(self.root, bg=self.bg_color)
        color_menu.pack(pady=20)

        tk.Label(color_menu, text='Изменить цвет фона:', font=('Arial', 16), bg=self.bg_color).pack(side=tk.LEFT)

        colors = {'Бежевый': 'beige',
                  'Светло-Зеленый': 'light green',
                  'Светло-Голубой': 'light blue'}

        def change_color(color):
            self.bg_color = color
            self.root.configure(bg=self.bg_color)
            self.create_main_menu()

        for color_name, color_code in colors.items():
            tk.Button(color_menu, text=color_name, command=lambda c=color_code: change_color(c), bg=color_code,
                      width=15, height=2, font=('Arial', 12)).pack(side=tk.LEFT, padx=10)

    def register_window(self):
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        tk.Label(self.root, text='Регистрация', font=('Arial', 24), bg=self.bg_color).pack(pady=20)

        tk.Label(self.root, text='Имя пользователя:', font=('Arial', 16), bg=self.bg_color).pack()
        username_entry = tk.Entry(self.root, font=('Arial', 16))
        username_entry.pack()

        tk.Label(self.root, text='Пароль:', font=('Arial', 16), bg=self.bg_color).pack()
        password_entry = tk.Entry(self.root, show='*', font=('Arial', 16))
        password_entry.pack()

        horoscope_var = tk.IntVar()
        tk.Checkbutton(self.root, text='Согласен на рассылку ежедневного гороскопа', variable=horoscope_var,
                       font=('Arial', 16), bg=self.bg_color).pack(pady=20)

        def register_action():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            if not username or not password:
                messagebox.showerror('Ошибка', 'Введите имя пользователя и пароль')
                return
            success = add_user(username, password, horoscope_var.get())
            if success:
                messagebox.showinfo('Успех', 'Регистрация прошла успешно')
                self.create_main_menu()
            else:
                messagebox.showerror('Ошибка', 'Пользователь уже существует')

        tk.Button(self.root, text='Зарегистрироваться', command=register_action, bg=self.bg_color, width=20, height=2,
                  font=('Arial', 16)).pack(pady=10)
        tk.Button(self.root, text='Назад', command=self.create_main_menu, bg=self.bg_color, width=20, height=2,
                  font=('Arial', 16)).pack(pady=10)

    def login_window(self):
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        tk.Label(self.root, text='Вход', font=('Arial', 24), bg=self.bg_color).pack(pady=20)

        tk.Label(self.root, text='Имя пользователя:', font=('Arial', 16), bg=self.bg_color).pack()
        username_entry = tk.Entry(self.root, font=('Arial', 16))
        username_entry.pack()

        tk.Label(self.root, text='Пароль:', font=('Arial', 16), bg=self.bg_color).pack()
        password_entry = tk.Entry(self.root, show='*', font=('Arial', 16))
        password_entry.pack()

        def login_action():
            username = username_entry.get().strip()
            password = password_entry.get().strip()
            if check_user(username, password):
                self.current_user = username
                messagebox.showinfo('Успех', f'Добро пожаловать, {username}!')
                self.user_menu()
            else:
                messagebox.showerror('Ошибка', 'Неверное имя пользователя или пароль')

        tk.Button(self.root, text='Войти', command=login_action, bg=self.bg_color, width=20, height=2,
                  font=('Arial', 16)).pack(pady=10)
        tk.Button(self.root, text='Назад', command=self.create_main_menu, bg=self.bg_color, width=20, height=2,
                  font=('Arial', 16)).pack(pady=10)

    def user_menu(self):
        self.clear_window()
        self.root.configure(bg=self.bg_color)
        tk.Label(self.root, text=f'Меню пользователя: {self.current_user}', font=('Arial', 24), bg=self.bg_color).pack(
            pady=20)

        def show_settings():
            horoscope_status = 'подписаны' if get_user_settings(self.current_user) else 'не подписаны'
            messagebox.showinfo('Настройки', f'Вы {horoscope_status} на ежедневный гороскоп.')

        def change_horoscope():
            def save_change():
                update_user_settings(self.current_user, var.get())
                messagebox.showinfo('Успех', 'Статус подписки обновлен')
                popup.destroy()

            popup = tk.Toplevel(self.root, bg=self.bg_color)
            popup.title('Изменить подписку на гороскоп')
            var = tk.IntVar(value=1 if get_user_settings(self.current_user) else 0)
            tk.Checkbutton(popup, text='Подписаться на ежедневный гороскоп', variable=var, font=('Arial', 16),
                           bg=self.bg_color).pack(padx=20, pady=20)
            tk.Button(popup, text='Сохранить', command=save_change, bg=self.bg_color, width=20, height=2,
                      font=('Arial', 16)).pack(pady=10)

        tk.Button(self.root, text='Посмотреть настройки', width=25, height=2, font=('Arial', 16), command=show_settings,
                  bg=self.bg_color).pack(pady=10)
        tk.Button(self.root, text='Отменить рассылку', width=25, height=2, font=('Arial', 16),
                  command=change_horoscope, bg=self.bg_color).pack(pady=10)
        tk.Button(self.root, text='Выйти из аккаунта', width=25, height=2, font=('Arial', 16), command=self.logout,
                  bg=self.bg_color).pack(pady=10)

    def logout(self):
        self.current_user = None
        messagebox.showinfo('Выход', 'Вы вышли из аккаунта')
        self.create_main_menu()


if __name__ == '__main__':
    init_db()
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()
