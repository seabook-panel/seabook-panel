import os
from flask import Blueprint, render_template, redirect
import config


from auth import auth
app = Blueprint('files', __name__)
appearance = config.get_config("appearance")

@app.route('/')
@auth
def index():
    return redirect('/files/'+config.get_config("server", "path"))

@app.route('/<path:dir>')
@auth
def path(dir):
    files = {
        "folders": [],
        "files": []
    }
    item_list = os.listdir(dir)
    for item in item_list:
        full_path = os.path.join(dir, item)
        if os.path.isdir(full_path):
            files['folders'].append({'name': item})
        if os.path.isfile(full_path):
            files['files'].append({'name': item,'path':full_path})
    print(files)
    return render_template('files/index.html', dir=dir, files=files, appearance=appearance)

@app.route('/edit/<path:dir>')
@auth
def edit(dir: str):
    with open(dir, "r") as f:
        content = f.read()
    edit_page = render_template('files/edit.html', dir=dir, content=content, appearance=appearance)
    return edit_page