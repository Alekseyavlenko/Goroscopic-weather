from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return f"""<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <title>Goroscopic-weather</title>
                      </head>
                      <body>
                        <h1>Добро пожаловать!!</h1>
                        <img src="{url_for('static', filename='img/title_image.png')}" 
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
    return f""""""


@app.route('/weather')
def weather():
    return f""""""


@app.route('/goroscope')
def goroscope():
    return f""""""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
