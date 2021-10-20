
import cv2

if __name__ == '__main__':

    img = cv2.imread("img/pic1.jpg", 1)

    imgB = img[:,:,1]

    cv2.imwrite("img/pic1_blue.jpg", imgB)

    cv2.imshow("img", imgB)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
