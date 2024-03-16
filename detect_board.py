import cv2
import numpy as np
from keras.models import load_model
from pred import predict

#model source: https://github.com/tempdata73/tic-tac-toe
model = load_model("model.h5")

def detect_board(img):

    global width, height

    if img is not None:

        width, height = img.shape

    width = width // 3

    height = height // 3

    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    for i in range(3):

        for j in range(3):

            sub_img = img[(i * width):((i+1)*width), (j*height):((j+1)*height)]

            #set threshold value for image processing
            threshold_value = 180

            max_value = 255

            sub_img = cv2.resize(sub_img, (32, 32))

            _, sub_img = cv2.threshold(sub_img, threshold_value, max_value, cv2.THRESH_BINARY)

            sub_img = 255 - sub_img
           
            move = predict(sub_img)

            board[i][j] = move

    return board


def perspective_transform(img):

    target_size = 320

    #define corner points as 2D array
    corner_pts = []

    corners = np.float32(corner_pts)

    target_corners = np.float32([[0, 0], [0, target_size], [target_size, 0], [target_size, target_size]])

    transform_matrix = cv2.getPerspectiveTransform(corners, target_corners)

    transformed_img = cv2.warpPerspective(img, transform_matrix, (target_size, target_size))

    return transformed_img
