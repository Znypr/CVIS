
import cv2
import functions

if __name__ == '__main__':

    images = []
    functions.set_window_size(200,200)

    # reading
    img = cv2.imread("img/forest/forest.jpeg", 1)
    images.append(["original", img])

    # filtering
    imgB = img[:,:,0]
    images.append(["blue", imgB])

    imgG = img[:,:,1]
    images.append(["green", imgG])

    imgR = img[:,:,2]
    images.append(["red", imgR])

    functions.save(images, "jpeg", "forest")
    functions.show(images)