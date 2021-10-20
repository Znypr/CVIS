import cv2

w, h = 600, 300

def set_window_size(width,height):
    global w, h
    w,h = width, height

def show(image):

    for i in range(len(image)):
        cv2.namedWindow(image[i][0], cv2.WINDOW_KEEPRATIO)
        cv2.imshow(image[i][0], image[i][1])
        cv2.resizeWindow(image[i][0], w, h)

    cv2.waitKey(0)
    cv2.destroyAllWindows()