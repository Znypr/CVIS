import cv2
import functions
import numpy as np



if __name__ == '__main__':

    images = []
    img = cv2.imread("img/bicycle/bike.png", 0)
    images.append(["original", img])

    img1 = cv2.Canny(img, 0,255)
    images.append(["canny", img1])

    img2 = cv2.Canny(img, 0, 255, apertureSize=5)
    images.append(["canny-aperture_5", img2])

    img3 = cv2.Canny(img, 0, 255, L2gradient=True)
    images.append(["canny-L2_true", img3])


    functions.save(images, "png", "bicycle")
    functions.show(images)
