"""
@File : recognition.py
@Author: Dong Wang
@Date : 2020/5/5
"""
from . import load_model, gestures, Sub2Model
from PIL import Image
import numpy as np
import six
import os


class recognition(object):
    def __init__(self, model):
        """
        Constructor of the abstract class. It is designed for common interface.
        You should implement a subclass of recognition firstly.

        # Usage:

        model = load_model(modelPath) # modelPath is a trained neural model.
        gR = gestureRecognition(model)
        for landmark in landmarks:
            gesture = gR.recognize(landmark)
            print("The gesture is ", gesture)

        """
        self.model = model

    def recognize(self, landmark):
        """ recognize gesture from an image
        :param landmark: landmark array
        :return:gesture
        """
        # landmark = landmark
        # # Do something to the landmark
        # gesture = self.model.predict(landmark)
        # return gesture
        raise NotImplementedError


class gestureRecognition(recognition):
    def __init__(self, model=Sub2Model):
        model = load_model(model)
        super(gestureRecognition, self).__init__(model=model)

    def recognize(self, landmark):
        response = {'code': 200}
        if len(landmark) != 80:
            response['code'] = 401
            return response
        elif isinstance(landmark, np.ndarray):
            # Img is Image type
            response['code'] = 200
            response['gesture'], response['probability'] = self.predict(landmark)
        else:
            response['code'] = 402
        return response

    def predict(self, pointsArray):
        if len(pointsArray.shape) == 1:
            pointsArray = np.array([pointsArray])
        pred = self.model.predict(pointsArray)[0]
        index = int(np.argmax(pred))
        gesture = gestures[index]
        return gesture, pred[index]
