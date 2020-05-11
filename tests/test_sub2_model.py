"""
@File : test_sub2_model.py
@Author: Dong Wang
@Date : 2020/5/11
"""

from RPSLSPlayer.core.recognition import gestureRecognition, np
import pytest

landmark = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                     0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 168,
                     139, 116, 106, 0, 0, 0, 0, 142, 65, 0, 0, 0, 0, 0, 0, 164, 68,
                     0, 0, 0, 0, 0, 0, 183, 75, 0, 0, 0, 0, 0, 0, 197, 83, 0, 0, 0, 0, 0, 0])


def test_sub2_model():
    gR = gestureRecognition(model='./Sub2-weights.hdf5')
    re = gR.recognize(landmark)
    print(re)


if __name__ == '__main__':
    test_sub2_model()
