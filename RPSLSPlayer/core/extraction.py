"""
@File : extraction.py
@Author: Dong Wang
@Date : 2020/5/5
"""


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
            print("We get landmarks are :", landmarks)

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
    def __init__(self, model):
        super(landmarkExtraction, self).__init__(model)

    def extract(self, img):
        pass
