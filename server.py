from flask import Flask, url_for, request

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


@app.route('/registration')
def registration():
    # from weather_request import pogoda_request
    return f"""hhhhhhhhhhhh"""


@app.route('/enter')
def enter():
    if request.method == 'GET':
        return f""" <form method="post">
            <label for="name">First Name:</label>
            <input type="text" id="name" name="name" placeholder="name">
            <label for="password">Password:</label>
            <input type="text" id="password" name="password" placeholder="password">
            <button type="submit">Enter</button>"""
    elif request.method == 'POST':
        return f"""{request.form['name']}"""


@app.route('/account')
def account(username):
    return f"""{username}"""


@app.route('/weather', methods=['POST', 'GET'])
def weather():
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


@app.route('/goroscope')
def goroscope():
    return f""""""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
