import cv2
from detect_board import perspective_transform, perspective_transform1, detect_board
from tictactoe import render_board

#define image path below
img_path = ""

img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

img = cv2.resize(img, (1000, 1000))

'''
define image corners below
should be a 2D array
'''
img_corners = []

img = perspective_transform(img)

while True:
    bd = detect_board(img)
    render_board(bd)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
