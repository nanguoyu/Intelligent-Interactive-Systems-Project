

# Intelligent Interactive Systems Project

[![Build Status](https://travis-ci.com/nanguoyu/Intelligent-Interactive-Systems-Project.svg?branch=master)](https://travis-ci.com/nanguoyu/Intelligent-Interactive-Systems-Project)
[![codecov](https://codecov.io/gh/nanguoyu/Intelligent-Interactive-Systems-Project/branch/master/graph/badge.svg)](https://codecov.io/gh/nanguoyu/Intelligent-Interactive-Systems-Project)



## What's this
This project aims to recognize 6 pre-defined gestures from videos.
As following images showing, there are 'fist_dorsal', 'fist_palm', 'open_dorsal', 'open_palm', 'three_fingers_dorsal', 'three_fingers_palm'.
![](.github/IIS_Project_gestures_example.png)

## Quick start
1. Install Opencv

    You should install Opencv in your environment.

2. git clone this project 

    ``` Python 
    git clone https://github.com/nanguoyu/Intelligent-Interactive-Systems-Project.git
    cd Intelligent-Interactive-Systems-Project
    pip install -r requirements.txt
    pip install .
    ```

3. Download pre-trained models
    ```
    python DownloadWeights.py
    ```

3. Start the API system and its extraction and recognition server:

    If your environment is windows 64, you should run [**start_app_win64.bat**](start_app_win64.bat) and do not close its window.
    
    If your environment is mac os/ linux, you should run [**start_app_macos.sh**](start_app_macos.sh) and do not close its window.

4. Run tests
    ```
    python tests/test_app.py
    ```
   You can check tests/test_app.py to send your image 
   to recognize gestures.
   
   ``` Python
   import base64
   import json
   import requests
   
   img_file = "open_dorsal.jpg"
   # URL = 'http://127.0.0.1:5000/gesture'
   URL = 'http://127.0.0.1:5000/end2end'
   """ post image and return the response """
   with open(img_file, 'rb') as f:
       img = base64.b64encode(f.read()).decode()
   response = requests.post(URL, data={"image": img})
   return json.loads(response.content.decode('utf-8'))
   ```


## Features
Bases on a unpublished data set, we are implementing these parts.
### landmark detection and gesture recognition
- [x] A landmark detection system
- [x] A machine learning based gesture recognition system
- [ ] A Kotlin program to control [Furhat](https://furhatrobotics.com/) Robot
- [x] An API for communication between the Kotlin program and Python Backend

### Specialization part.
- [x] An end-to-end system (CNN) 

<div align="center">
    <img src=".github/rule.png">
</div>


#### Demo for the end2end detection model
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/I9NC9vfVFQM/0.jpg)](https://www.youtube.com/watch?v=I9NC9vfVFQM)


## Reference
- [The Supervised Machine Learning book(An upcoming textbook)](http://smlbook.org/)
- [SemiFlow](https://github.com/nanguoyu/SemiFlow)
