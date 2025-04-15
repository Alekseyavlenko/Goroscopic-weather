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
                        <a href="http://127.0.0.1:8080/registration">
                        <button type=submit>Register</button>
                        </a>
                        <h4>здесь мы будем прогнозировать погоду</br>
                        (с гороскопом!!!)</h4>
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
