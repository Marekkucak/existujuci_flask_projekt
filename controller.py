from flask import Flask, render_template
import os
from model import Model

app = Flask(__name__)

model = Model('rss_parser_data.db')

@app.route("/")
def view():
    return render_template('view.html', articles_list=model.select_everything())
