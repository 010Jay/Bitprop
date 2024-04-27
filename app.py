#!flask/bin/python
from flask import Flask

from controller.UserController import user_api

app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, Wellcome to my Bitprop Project!"


# Add blueprints for the different api's
app.register_blueprint(user_api)

if __name__ == '__main__':
    app.run(threaded=False)
