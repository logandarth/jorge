from flask import Flask

app = Flask("meu app")

@app.route('/')

def hello():
    return "<h1>helou parça</h1>"

@app.route('/ola')
def ola():
    return "<h1>ola de novo</h1>"


