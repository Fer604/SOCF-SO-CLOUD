from flask import Flask

APP = Flask(__name__)


@APP.get("/")
def index():
    return "<h1>cole familia</h1>"

@APP.get("/info")
def info():
    return "Integrantes: \nAndré Esteves Arantes \nFernando Aschwanden \nGustavo Jansen"

if __name__ == '__main__':
    APP.run(host='0.0.0.0',port=80)
