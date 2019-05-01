from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '6b3999f097cd48641b3cc38e8d5a3f88'

from MessMatrix import routes
