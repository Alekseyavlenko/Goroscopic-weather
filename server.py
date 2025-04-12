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
                        <h1>Жди нас, Марс!</h1>
                        <img src="{url_for('static', filename='img/title_image.png')}" 
                            alt="здесь должна была быть картинка, но не нашлась">
                        <h4>здесь мы будем прогнозировать погоду</br>
                        (с гороскопом!)</h4>
                      </body>
                    </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
