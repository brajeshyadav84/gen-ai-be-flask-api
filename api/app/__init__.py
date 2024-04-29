from flask import Flask
flask_app = Flask(__name__)

#
# All API routing defined here 
#

from app.api_endpoints import home
from app.api_endpoints import project
from app.api_endpoints import watson
