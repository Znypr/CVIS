import cv2
import imghdr

w, h = 600, 300

def set_window_size(width,height):
    global w, h
    w,h = width, height

def show(images):

    for i in range(len(images)):
        cv2.namedWindow(images[i][0], cv2.WINDOW_KEEPRATIO)
        cv2.imshow(images[i][0], images[i][1])
        cv2.resizeWindow(images[i][0], w, h)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save(images, type, folder):


    for i in range(1, len(images)):
        path = "img/" + folder +"/"+ folder + "_" + images[i][0] + "." + type
        cv2.imwrite(path, images[i][1])