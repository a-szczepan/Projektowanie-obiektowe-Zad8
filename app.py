from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'A. Szczepanczyk - projektowanie obiektowe, zadanie 8'
