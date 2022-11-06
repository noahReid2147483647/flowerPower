import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
import numpy as np
import cv2


def flower_prediction(filepath):
    # Import ML Model
    model = tf.keras.models.load_model('my_model')

    # All Image Categories
    categories = ['Daisy', 'Dandelion', 'Rose', 'Sunflower', 'Tulip']

    # path = 'C:/Users/visha/Flower_Image_Recognition_Project/pythonProject/User_Input/UserImage.jpg'

    # Convert input image to Numpy Array
    img = tf.keras.preprocessing.image.load_img(filepath)
    img_data = tf.keras.preprocessing.image.img_to_array(img, data_format=None, dtype=None)
    img_data = cv2.resize(img_data, (180, 180))
    input_arr = np.array([img_data])

    # Generate Prediction from input image
    classification = model.predict(input_arr)
    prediction = categories[np.argmax(classification[0])]
    confidence = classification[0][np.argmax(classification)]

    # print(prediction)
    # print(confidence)

    return [prediction, confidence]
