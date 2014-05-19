from flask import Flask, jsonify, render_template, request, redirect, url_for
app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(message='hello world!')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
