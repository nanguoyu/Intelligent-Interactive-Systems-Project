"""
@File : recognition.py
@Author: Dong Wang
@Date : 2020/5/5
"""


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
    def __init__(self, model):
        super(gestureRecognition, self).__init__(model=model)

    def recognize(self, landmark):
        pass
