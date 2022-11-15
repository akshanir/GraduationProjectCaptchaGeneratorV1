import tensorflow as tf
from keras.api._v2.keras import layers,models,datasets
import os
import time
import json
import glob
#from generator import get_captcha_image
import matplotlib.pyplot as plt
from PIL import Image

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

tf.__version__
model = tf.keras.models.load_model('my_model.h5')

# Check its architecture
model.summary()

def format_y(y):
    return ''.join(map(lambda x: chr(int(x)), y))


def predict(image_path):
    im = Image.open(image_path).convert('RGB')
    # im = im.resize((H, W))
    im = np.array(im) / 255.0
    im = np.array(im)
    y_pred = model.predict(np.array([im]))
    y_pred = tf.math.argmax(y_pred, axis=-1)
    
    print('predict: %s' % format_y(y_pred[0]))
    return format_y(y_pred[0])
    # plt.imshow(im)


