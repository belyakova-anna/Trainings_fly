from flask import render_template
from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index/<username>')
def index(username):
    return render_template('base.html', title=username)


@app.route('/training/<prof>')
def training(prof):
    return render_template('index.html', title='', profession=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
