import numpy as np
import cv2
from keras.models import load_model

#model source: https://github.com/tempdata73/tic-tac-toe
model = load_model("model.h5")


def predict(image):

    image = (cv2.resize(image, (32, 32)))

    image = np.expand_dims(image, axis=-1)

    image = np.expand_dims(image, axis=0)

    lst = model.predict(image)

    pred = np.argmax(lst)

    if pred == 0:

        return ""

    elif pred == 1:

        return "X"

    else:

        return "O"
