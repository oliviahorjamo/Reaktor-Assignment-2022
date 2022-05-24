from app import app
from flask import render_template, redirect, request
from parsing.parser import parser

@app.route("/", methods = ["GET", "POST"])
def give_file():
    if request.method == "GET":
        return render_template("input_file.html")
    elif request.method == "POST":
        file_to_parse = request.form["file_to_parse"]
        parser.set_file(file=file_to_parse)
        parser.parse_file()
    return redirect("/index")

@app.route("/index", methods = ["GET", "POSt"])
def index():
    if request.method == "GET":
        return render_template("index.html", packages = parser.parsed_packages)


