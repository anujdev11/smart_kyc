from flask import Flask, render_template, Response,redirect,url_for,jsonify,request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1',debug=True)