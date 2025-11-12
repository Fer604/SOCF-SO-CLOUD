from flask import Flask, render_template_string, jsonify
import data

APP = Flask(__name__)

@APP.get("/")
def index():
    return "<h1>cole familia</h1>"

@APP.get("/metricas")
def metricas():
    r = {
        "Nomes": data.get_names(),  
        "Proccess ID": str(data.get_PID()),
        "Memória usada": str(data.get_ram_usage()),
        "CPU": str(data.get_cpu_usage()),
        "SO": data.get_os()
    }
    res = jsonify(r)

    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Métricas</title>
            <style>
                body { font-family: sans-serif; margin: 2em; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>Dados:</h1>
            <p>{{ data }}</p>
        </body>
        </html>
        """, data = res)

@APP.get("/info")
def info():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Info</title>
            <style>
                body { font-family: sans-serif; margin: 2em; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>Nomes:</h1>
            <p>{{ name }}</p>
        </body>
        </html>
        """, name = data.get_names())

if __name__ == '__main__':
    APP.run(host='0.0.0.0',port=80)
