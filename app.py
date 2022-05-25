from flask import Flask

app = Flask(__name__, template_folder="./ui/templates", static_folder="./ui/static")

from ui.src import routes