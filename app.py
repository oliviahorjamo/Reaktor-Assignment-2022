from flask import Flask

app = Flask(__name__, template_folder="./ui/templates")

from ui.src import routes