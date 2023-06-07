from app import app
from flask import render_template, request
from datetime import datetime
from.forms import UserNameForm

@app.route ('/', methods=['GET'])
@app.route('/index')
def index():
        form = UserNameForm()
        return render_template ("index.html", form = form);

@app.route ('/', methods=['POST'])
def index_post():
#         text = request. form ['user_name']
        form = UserNameForm()
        if form.validate_on_submit():
                text = form.UserNameField.data
                return render_template ("index.html", form = form, user_name = text);
        else:
                return "Bad form"