
import cv2
import functions

if __name__ == '__main__':


    # reading
    img = cv2.imread("img/forest/forest.jpeg", 1)

    # filtering
    imgB = img[:,:,0]
    imgG = img[:,:,1]
    imgR = img[:,:,2]

    # saving
    cv2.imwrite("img/forest/pic1_blue.jpg", imgB)
    cv2.imwrite("img/forest/pic1_green.jpg", imgG)
    cv2.imwrite("img/forest/pic1_red.jpg", imgR)

    images = []
    functions.set_window_size(200,200)

    images.append(["original", img])
    images.append(["blue", imgB])
    images.append(["green", imgG])
    images.append(["red", imgR])

    functions.show(images)