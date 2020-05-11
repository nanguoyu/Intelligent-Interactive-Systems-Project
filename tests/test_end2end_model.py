"""
@File : test_end2end_model.py
@Author: Dong Wang
@Date : 2020/5/9
"""
from RPSLSPlayer.core.end2end import end2endGesture, load_img, img_to_array
import pytest


def test_end2end_model():
    # Model Path
    imageFile = 'fist_dorsal.jpg'
    eG = end2endGesture(model='End2endWeights-best.hdf5')
    img = load_img(imageFile)
    re = eG.recognize(img)
    print(re)


if __name__ == '__main__':
    test_end2end_model()
