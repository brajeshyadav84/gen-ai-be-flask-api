from app import flask_app
from flask import request

@flask_app.route("/api/home", methods =["GET","POST"])
def home():
    request_json = request.get_json()
    if request_json:
        user_name = request_json["userName"]
    else:
        user_name =None
    return f"Welcome to my APP - Welcome {user_name}"
