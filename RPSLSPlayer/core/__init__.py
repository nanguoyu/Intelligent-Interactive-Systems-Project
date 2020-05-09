"""
@File : __init__.py
@Author: Dong Wang
@Date : 2020/5/5
"""
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img, array_to_img
import cv2

cols = ['palm_root_x', 'palm_root_y', 'palm_thumb_1_x', 'palm_thumb_1_y',
        'palm_thumb_2_x', 'palm_thumb_2_y', 'palm_thumb_3_x',
        'palm_thumb_3_y', 'palm_index_1_x', 'palm_index_1_y',
        'palm_index_2_x', 'palm_index_2_y', 'palm_index_3_x',
        'palm_index_3_y', 'palm_index_4_x', 'palm_index_4_y',
        'palm_middle_1_x', 'palm_middle_1_y', 'palm_middle_2_x',
        'palm_middle_2_y', 'palm_middle_3_x', 'palm_middle_3_y',
        'palm_middle_4_x', 'palm_middle_4_y', 'palm_ring_1_x',
        'palm_ring_1_y', 'palm_ring_2_x', 'palm_ring_2_y', 'palm_ring_3_x',
        'palm_ring_3_y', 'palm_ring_4_x', 'palm_ring_4_y',
        'palm_pinky_1_x', 'palm_pinky_1_y', 'palm_pinky_2_x',
        'palm_pinky_2_y', 'palm_pinky_3_x', 'palm_pinky_3_y',
        'palm_pinky_4_x', 'palm_pinky_4_y', 'dorsal_root_x',
        'dorsal_root_y', 'dorsal_thumb_1_x', 'dorsal_thumb_1_y',
        'dorsal_thumb_2_x', 'dorsal_thumb_2_y', 'dorsal_thumb_3_x',
        'dorsal_thumb_3_y', 'dorsal_index_1_x', 'dorsal_index_1_y',
        'dorsal_index_2_x', 'dorsal_index_2_y', 'dorsal_index_3_x',
        'dorsal_index_3_y', 'dorsal_index_4_x', 'dorsal_index_4_y',
        'dorsal_middle_1_x', 'dorsal_middle_1_y', 'dorsal_middle_2_x',
        'dorsal_middle_2_y', 'dorsal_middle_3_x', 'dorsal_middle_3_y',
        'dorsal_middle_4_x', 'dorsal_middle_4_y', 'dorsal_ring_1_x',
        'dorsal_ring_1_y', 'dorsal_ring_2_x', 'dorsal_ring_2_y',
        'dorsal_ring_3_x', 'dorsal_ring_3_y', 'dorsal_ring_4_x',
        'dorsal_ring_4_y', 'dorsal_pinky_1_x', 'dorsal_pinky_1_y',
        'dorsal_pinky_2_x', 'dorsal_pinky_2_y', 'dorsal_pinky_3_x',
        'dorsal_pinky_3_y', 'dorsal_pinky_4_x', 'dorsal_pinky_4_y']

gestures = ['fist_dorsal', 'fist_palm', 'open_dorsal',
            'open_palm', 'three_fingers_dorsal', 'three_fingers_palm']

Sub1Model = './model/Sub1-weights-best.hdf5'
end2endModel = './model/End2endWeights-best.hdf5'
