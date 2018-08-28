# -*- coding: utf-8 -*-

from flask import Flask
from p2p.api import api


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.register_blueprint(api)
    return app