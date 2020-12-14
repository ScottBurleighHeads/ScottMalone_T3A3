# Implement an ORM with pyth and flask.
from dotenv import load_dotenv
load_dotenv()

import database                                 

from flask import Flask
app = Flask(__name__)

from controllers import registerable_controllers
for controller in registerable_controllers:
    app.register_blueprint(controller)               # Registers the endpoints on the blueprint from endpoints.py



