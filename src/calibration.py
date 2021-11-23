import glob

import cv2
import numpy as np


class chessboard: x, y = 6, 9


# termination criteria
criteria = (
    cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object vectors, like (0,0,0), (1,0,0), (2,0,0) ....,
# (grid.x,5,0)
objv = np.zeros((chessboard.x * chessboard.y, 3), np.float32)
objv[:, :2] = np.mgrid[:chessboard.x, :chessboard.y].T.reshape(-1, 2)

vectors_3d = []  # 3d vector in real world space
vectors_2d = []  # 2d vector in image plane

images = glob.glob('../img/chess/*.jpg')

for image in images:

    # 1.1 Reading
    img = cv2.imread(image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 1.2 Detect Corners
    successful_retrieval, corners = cv2.findChessboardCorners(
        gray,
        (chessboard.x, chessboard.y),
        None
    )

    if successful_retrieval:
        vectors_3d.append(objv)
        vectors_2d.append(corners)
        # corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1,
        # -1), criteria)

        # 1.3 Display Corners
        cv2.drawChessboardCorners(
            img,
            (chessboard.x, chessboard.y),
            corners,
            successful_retrieval
        )
        # cv2.imshow('img', img)
        # cv2.waitKey(5)

# cv2.destroyAllWindows()

# 1.4 Calibration
error, K, distCoeffs, R, t = cv2.calibrateCamera(
    vectors_3d,
    vectors_2d,
    gray.shape[::-1],
    None,
    None
)

# 2.2
fx, cx = 460, 310
fx = input("fx:") # 460
cx = input("cx:") # 310
K[0][0] = fx
K[0][2] = cx

output = {
    "error": error, "K": K, "distCoeffs": distCoeffs, "R": R[0],
    "t":     t[0]
}
for k, v in output.items():
    print("\n\t{}\n{}".format(k, v))



# 1.5
corners_3d = objv

for i in range(len(images)):
    corners_2d, _ = cv2.projectPoints(
        corners_3d, R[i], t[i], K,
        distCoeffs
    )
    img = cv2.imread(images[i])
    cv2.drawChessboardCorners(
        img,
        (chessboard.x, chessboard.y),
        corners_2d,
        successful_retrieval
    )
    cv2.imshow("test", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
