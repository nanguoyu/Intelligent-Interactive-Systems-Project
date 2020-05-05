"""
@File : app.py.py
@Author: Dong Wang
@Date : 2020/5/5
"""
from flask import Flask
from . import __version__
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, this is the server of RPSLSPlayer agent. \n Version: '+__version__
