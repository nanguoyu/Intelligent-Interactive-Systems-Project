"""
@File : app.py.py
@Author: Dong Wang
@Date : 2020/5/5
"""
from flask import Flask, request
import base64
import numpy as np
from . import __version__

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello, this is the server of RPSLSPlayer agent. \n Version: ' + __version__


@app.route("/gesture", methods=['POST', 'GET'])
def gesture():
    image = request.form.get('image')
    if not image:
        return 'not found image file'
    img = base64.b64decode(str(image))
    image_data = np.fromstring(img, np.uint8)

    # Here we should do something to recognize the image_data

    return {'code': 200, 'gesture': 'open_palm'}
