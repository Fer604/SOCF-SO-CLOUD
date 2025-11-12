from flask import Flask, render_template_string, jsonify
import data

APP = Flask(__name__)

@APP.get("/")
def index():
    return render_template_string("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Bem vindo!</title>
            <style>
                body { font-family: sans-serif; margin: 2em; }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <a href="/metricas">Métricas</a>
            <a href="/info">Info</a>
        </body>
        </html>
        """)

@APP.get("/metricas")
def metricas():
    res = {
        "Nomes": data.get_names(),  
        "\nProccess ID": str(data.get_PID()),
        "\nMemória usada": str(data.get_ram_usage()),
        "\nCPU": str(data.get_cpu_usage()),
        "\nSO": data.get_os()
    }

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
        """, data = jsonify({res}))

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
            <ul>
                {% for name in names %}
                    <li>{{ name }}</li>
                {% endfor %}
            </ul>
        </body>
        </html>
        """, names = data.get_names())

if __name__ == '__main__':
    APP.run(host='0.0.0.0',port=80)
