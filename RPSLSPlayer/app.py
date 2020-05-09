"""
@File : app.py.py
@Author: Dong Wang
@Date : 2020/5/5
"""
from flask import Flask, request
import base64
from io import BytesIO
import numpy as np
from . import __version__
from .core.extraction import landmarkExtraction, Image, img_to_array

# Model Path
Sub1Model = './RPSLSPlayer/model/Sub1-weights-best.hdf5'

#
app = Flask(__name__)


lE = landmarkExtraction(Sub1Model)


@app.route('/')
def index():
    return 'Hello, this is the server of RPSLSPlayer agent. \n Version: ' + __version__


@app.route("/gesture", methods=['POST', 'GET'])
def gesture():
    image = request.form.get('image')
    if not image:
        return 'not found image file'
    IM = Image.open(BytesIO(base64.b64decode(image)))
    # SubSystem 1
    re1 = lE.extract(IM)
    if re1['code'] == 200:
        keypoints = re1['keypoints']
    else:
        keypoints = None

    # SubSystem 2
    # TODO SubSystem
    response = {'code': 200, 'gesture': 'open_palm', 'keypoints': keypoints}
    return response
