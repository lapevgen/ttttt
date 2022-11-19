import os

from flask import Flask

app = Flask(__name__)
#nnn


@app.route("/")
def index():
    return "Привет от приложения Flask"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

# http://127.0.0.1:5000/