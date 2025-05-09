from flask import Flask, url_for, request, redirect, render_template

app = Flask(__name__)


@app.route('/')
def index():
    background = "body {background-color: #002f55; }"
    text = "h1 {color: #ffffff; } h3 {color: #ffffff; } h4 {color: #ffffff; } h2 {color: #000000; }"
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Goroscopic-weather</title>
                        <style> {background} {text} </style>
                        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                      </head>
                      <body>
                        <h1 class="">Добро пожаловать!!</h1>
                        <img id="greeting_image" src="{url_for('static', filename='img/title_image.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <br>
                        <p>
                        <a href="http://127.0.0.1:8080/registration">
                        <button type=submit><h2>Зарегистрироваться<h2></button>
                        </a>
                        <h4>или</h4>
                        <a href="http://127.0.0.1:8080/enter">
                        <button type=submit><h2>Войти<h2></button>
                        </a>
                        </p>
                        <h3>
                        Приложение для прогноза погоды и гороскопа — это веб-приложение,<br>
                        которое объединяет функции отображения текущей погоды и прогноза на несколько дней вперёд,<br>
                        а также предоставляет пользователям ежедневные гороскопы.<br><br>
                        Основные функции:<br> Прогноз погоды: отображение текущей погоды, поиск погоды по городам.<br>
                        Гороскоп: ежедневные гороскопы для всех знаков зодиака,<br>
                        возможность выбора знака зодиака для просмотра персонализированного гороскопа.
                        </h3>
                      </body>
                    </html>"""


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'GET':
        return f"""
            <form method="post">
                <label>Имя пользователя: <input type="text" name="username" required></label><br>
                <label>Пароль: <input type="password" name="password" required></label><br>
                <label>Нужен ли гороскоп? <input type="checkbox" name="wants_horoscope" checked></label><br>
                <input type="submit" value="Зарегистрироваться">
            </form>
                """
    elif request.method == 'POST':
        from registration import save_user
        username = request.form['username']
        password = request.form['password']
        wants_horoscope = 'wants_horoscope' in request.form
        save_user(username, password, 1 if wants_horoscope else 0)
        return redirect(f'http://127.0.0.1:8080/account/{username}')


@app.route('/enter', methods=['GET', 'POST', ])
def enter():
    if request.method == 'GET':
        return f""" <form method="post">
            <label for="name">First Name:</label>
            <input type="text" id="name" name="name" placeholder="name">
            <label for="password">Password:</label>
            <input type="text" id="password" name="password" placeholder="password">
            <button type="submit">Войти</button>"""
    elif request.method == 'POST':
        import csv
        with open('data/users.csv', encoding="utf8") as users_file:
            reader = csv.reader(users_file, delimiter=';', quotechar='"')
            title = next(reader)
            for i in reader:
                h = request.form['name']
                if h == i[1] and request.form['password'] == i[2]:
                    return redirect(f'http://127.0.0.1:8080/account/{h}')
            return f"""Данный пользователь не найден.<br>Неправильное имя или пароль"""


@app.route('/account/<username>', methods=['POST', 'GET'])
def account(username):
    import csv
    with open('data/users.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';', quotechar='"')
        title = next(reader)
        goroscop = ''
        for row in reader:
            if username == row[1]:
                if row[-1]:
                    goroscop = f"""<h4>или</h4>
                        <a href="http://127.0.0.1:8080/goroscope/{username}">
                        <button type=submit><h2>Гороскоп<h2></button>
                        </a>"""
                break
    return f"""<a href="http://127.0.0.1:8080/weather/{username}">
                        <button type=submit><h2>Погода<h2></button>
                        </a>
                        {goroscop}
                        """


@app.route('/weather/<username>', methods=['POST', 'GET'])
def weather(username):
    if request.method == 'GET':
        return f""" <form method="post">
            <label for="city">Город</label>
            <input type="text" id="city" name="city" placeholder="city">
            <label for="country">Страна</label>
            <input type="text" id="country" name="country" placeholder="country">
            <button type="submit">Погода</button>"""
    elif request.method == 'POST':
        from weather_request import pogoda_request
        return f"""{pogoda_request(request.form['city'], request.form['country'])}"""


@app.route('/goroscope/<username>', methods=['POST', 'GET'])
def goroscope(username):
    if request.method == 'GET':
        return render_template('goroscope.html', username=username)
    elif request.method == 'POST':
        from presckazaniye import get_random_prediction
        return get_random_prediction(request.form['class'])


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
