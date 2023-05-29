from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Método para regresar al inicio.
@app.route('/index.html')
def index():
    return render_template('index.html')