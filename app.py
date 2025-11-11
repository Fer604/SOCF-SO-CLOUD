from flask import Flask, jsonify
import data

APP = Flask(__name__)


@APP.get("/")
def index():
    return "<h1>cole familia</h1>"

@APP.get("/metricas")
def index():
    d = {
        "Nome": "",
        "Proccess ID": "",
        "Memória usada": data.get_ram_usage,
        "CPU": data.get_cpu_usage
    }
    return jsonify(d)

@APP.get("/info")
def info():
    names = data.get_names()

    for name in names:
        return {
            "Nome": name
        }

if __name__ == '__main__':
    APP.run(host='0.0.0.0',port=80)
