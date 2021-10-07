from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    ''' this is a main page of site '''
    return 'Hello'
