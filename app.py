from flask import Flask, render_template, jsonify
import pandas as pd
import json


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


# turn into json format



@app.route('/')
def index():  # put application's code here
    with open("static/data/criminals.json", 'r') as file:
        json_data = json.load(file)
    criminals_json = json.dumps(json_data)

    with open("static/data/superheroes.json", 'r') as file2:
        json_data2 = json.load(file2)
    superheroes_json = json.dumps(json_data2)

    return render_template('index.html', criminals=criminals_json, superheroes=superheroes_json)


if __name__ == '__main__':
    app.run(debug=True)
