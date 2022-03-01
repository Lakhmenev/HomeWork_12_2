from flask import Flask
from main.main import main
from loader.loader import loader


app = Flask(__name__)
app.register_blueprint(main)
app.register_blueprint(loader)


if __name__ == '__main__':
    app.debug = True
    app.run(host="127.0.0.1", port=5000)
