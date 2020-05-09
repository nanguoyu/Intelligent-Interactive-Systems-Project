"""
@File : extraction.py
@Author: Dong Wang
@Date : 2020/5/5
"""
from . import load_model, cv2, cols, img_to_array, load_img, array_to_img, Sub1Model
from PIL import Image
import numpy as np
import six
import os


class extraction(object):
    def __init__(self, model):
        """
        Constructor of the abstract class. It is designed for common interface.
        You should implement a subclass of extraction firstly.

        # Usage:

        model = load_model(modelPath) # modelPath is a trained neural model.
        lE = landmarkExtraction(model)
        for frame in videos:
            landmarks = lE.extract(frame)
            print("The landmarks are :", landmarks)

        """
        self.model = model

    def extract(self, img):
        """ extract landmarks from an image
        :param img: frame or image array
        :return: landmarks
        """
        # img = img
        # # Do something to the img
        # landmarks = self.model.predict(img)
        # return landmarks
        raise NotImplementedError


class landmarkExtraction(extraction):
    def __init__(self, model=Sub1Model):
        # Load .hdf5
        model = load_model(model)
        super(landmarkExtraction, self).__init__(model)

    def extract(self, img):
        response = {'code': 200}
        if isinstance(img, six.string_types):
            # Img is str type
            response['code'] = 501
            return response
        elif isinstance(img, Image.Image):
            # Img is Image type
            response['code'] = 200
            img = img.resize((320, 240), Image.LANCZOS)
            image = img_to_array(img)
            response['keypoints'] = self.predict(image)
        else:
            response['code'] = 502
        return response

    def predict(self, imgArray):
        if len(imgArray.shape) == 3:
            imgArray = np.array([imgArray/255])
        pred = self.model.predict(imgArray)[0]
        pred = pred * 255
        pred[pred < 20] = 0  # TODO Remove negative value but cannot extract finger in left-up
        keypoints = pred.astype(int)
        result = {}
        for i in range(len(cols)):
            result[cols[i]] = int(keypoints[i])
        return result

