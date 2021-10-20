import cv2
import functions

if __name__ == '__main__':

    images = []

    img = cv2.imread("img/street/street.png", 1)
    images.append(["original", img])



    functions.show(images)

