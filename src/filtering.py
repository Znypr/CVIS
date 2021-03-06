import cv2

import functions

if __name__ == '__main__':
    images = []

    img = cv2.imread("../img/chess/left2.jpg", 1)
    images.append(["Original", img])

    # 1. 5x5 Smoothing
    # img1 = functions.blur(img, 5)
    # images.append(["5x5-Smoothing", img1])

    # 2. 3x3 Smoothing
    # img2 = functions.blur(img, 3)
    # images.append(["3x3-Smoothing", img2])

    # 3. X Gradient
    img3 = functions.filter_custom(
        img, [[-1, 0, 1],  # Prewitt top>bottom
              [-1, 0, 1],
              [-1, 0, 1]]
    )

    # img3 = cv2.Sobel(img, -1, 1, 0) #Sobel
    images.append(["X-Gradient", img3])

    # 4. Y Gradient
    img4 = functions.filter_custom(
        img, [[-1, 0, 1],  # Prewitt left>right
              [-1, 0, 1], [-1, 0, 1]]
    )
    # img5 = cv2.Sobel(img, -1, 1, 0) #Sobel
    #images.append(["Y-GradientP", img4])

    # 5. LaPlace
    # img5 = functions.filter_custom(
    # img, [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
    # )
    # images.append(["LaPlace", img5])

    # functions.save(images, "png", "street")
    functions.show(images)
