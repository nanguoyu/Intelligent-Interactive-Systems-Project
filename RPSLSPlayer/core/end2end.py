"""
@File : end2end.py
@Author: Dong Wang
@Date : 2020/5/9
"""
from . import load_model, cv2, cols, img_to_array, load_img, array_to_img, end2endModel, gestures
from PIL import Image
import numpy as np
import six


class end2endGesture(object):
    def __init__(self, model=end2endModel):
        self.model = load_model(model)

    def recognize(self, img):
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
            response['gesture'], response['probability'] = self.predict(image)
        else:
            response['code'] = 502
        return response

    def predict(self, imgArray):
        if len(imgArray.shape) == 3:
            imgArray = np.array([imgArray/255])
        pred = self.model.predict(imgArray)[0]
        index = int(np.argmax(pred))
        gesture = gestures[index]
        return gesture, pred[index]
