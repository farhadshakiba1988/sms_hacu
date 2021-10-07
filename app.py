from flask import Flask

app = Flask(__name__)


@app.route('/')
def main_page():
    ''' this is a main page of site '''
    return 'Hello'


@app.route('/v1/get_sms')
def get_sms():
    pass


@app.route('/v1/send_sms')
def send_sms():
    pass


@app.route('/v1/check_serial')
def check_serial():
    pass
