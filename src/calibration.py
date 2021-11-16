import glob

import cv2
import numpy as np

class chessboard: x, y = 6, 9

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object vectors, like (0,0,0), (1,0,0), (2,0,0) ....,(grid.x,5,0)
objv = np.zeros((chessboard.x * chessboard.y, 3), np.float32)
objv[:, :2] = np.mgrid[:chessboard.x, :chessboard.y].T.reshape(-1, 2)

vectors_3d = []  # 3d vector in real world space
vectors_2d = []  # 2d vector in image plane.

images = glob.glob('img/chess/*.jpg')

for image in images:
    
    #1 Reading
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #2 Detect Corners
    successful_retrieval, corners = cv2.findChessboardCorners(gray, (chessboard.y, chessboard.x), None)
    
    if successful_retrieval:
        vectors_3d.append(objv)
        vectors_2d.append(corners)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)

        #3 Display Corners
        cv2.drawChessboardCorners(img, (chessboard.y, chessboard.x), corners2, successful_retrieval)
        cv2.imshow('img', img)
        cv2.waitKey(10)
        
cv2.destroyAllWindows()

#4 Calibration
successful_retrieval, K, distCoeffs, R, t = cv2.calibrateCamera(vectors_3d, vectors_2d, gray.shape[::-1], None, None)

#5 ?
