"""
@File : test_sub1_model.py
@Author: Dong Wang
@Date : 2020/5/9
"""
from RPSLSPlayer.core.extraction import landmarkExtraction, load_img, img_to_array
import pytest


def test_sub1_model():
    # Model Path
    imageFile = 'fist_dorsal.jpg'
    lE = landmarkExtraction(model='Sub1-weights-best.hdf5')
    img = load_img(imageFile)
    re = lE.extract(img)
    print(re)
    print(list(re['keypoints'].values()))


if __name__ == '__main__':
    test_sub1_model()
