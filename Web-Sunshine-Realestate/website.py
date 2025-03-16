from flask import Flask
from Home import home


app = Flask(__name__)
app.register_blueprint(home, url_prefix="/trifecta-properties")#, name="Liam")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
