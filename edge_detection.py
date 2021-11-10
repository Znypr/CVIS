import cv2
import functions

if __name__ == '__main__':
    images = []
    img = cv2.imread("img/bicycle/bike.png", 1)
    images.append(["original", img])

    img2 = cv2.Canny(img, 100, 200)
    images.append(["canny-1", img2])

    img3 = cv2.Canny(img, 200, 200)
    images.append(["canny-2", img3])

    img4 = cv2.Canny(img, 100, 100)
    images.append(["canny-3", img4])

    functions.save(images, "png", "bicycle")
    functions.show(images)
