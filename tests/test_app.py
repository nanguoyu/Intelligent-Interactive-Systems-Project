"""
@File : test_app.py
@Author: Dong Wang
@Date : 2020/5/5
"""
import base64
import json
import requests


def test_post_image(img_file, URL):
    """ post image and return the response """
    with open(img_file, 'rb') as f:
        img = base64.b64encode(f.read()).decode()
    response = requests.post(URL, data={"image": img})
    return json.loads(response.content.decode('utf-8'))


if __name__ == '__main__':
    # print(test_post_image('open_dorsal.jpg', 'http://127.0.0.1:5000/gesture'))
    print(test_post_image('open_dorsal.jpg', 'http://127.0.0.1:5000/end2end'))
