import cv2
import functions
import numpy as np

ddepth = 0

anchor = 0
delta = 0 #optional

if __name__ == '__main__':

    images = []

    img = cv2.imread("img/street/street.png", 1)
    images.append(["Original", img])


    # 1. 5x5 Smoothing
    kernel = np.ones((5,5))
    kernel = kernel/sum(kernel)**2

    img1 = cv2.filter2D(img, -1, kernel)
    #images.append(["5x5_Smoothing", img1])

    # 2. 3x3 Smoothing
    kernel = np.ones((3,3))
    kernel = kernel/sum(kernel)**2

    img2 = cv2.filter2D(img, -1, kernel)
    #images.append(["3x3_Smoothing", img2])

    # 3. X Gradient
    #img3 = cv2.filter2D()
    #images.append(["X_Gradient", img3])

    # 4. Y Gradient
    #img4 = cv2.filter2D()
    #images.append(["Y_Gradient", img4])

    # 5. LaPlace
    kernel = np.array([[0,1,0],[1,-4,1],[0,1,0]])

    img5 = cv2.filter2D(img, -1, kernel)
    images.append(["LaPlace", img5])

    #functions.save(images, "png", "street")
    functions.show(images)

