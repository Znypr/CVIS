import copy
import os
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

w, h = 500, 500


def set_window_size(width, height):
    global w, h
    w, h = width, height

def read_folder(path, flag):
    set = []
    for img in os.listdir(path):
        set.append(cv2.imread(path+"/"+img, flag))

    return set

def show(images, more_images=None, title=None):

    if more_images:
        for img in more_images:
            images.append(img)

    for i in range(len(images)):
        if isinstance(type(images[i][0]), str):
            cv2.namedWindow(images[i][0], cv2.WINDOW_KEEPRATIO)
            cv2.imshow(images[i][0], images[i][1])
            cv2.resizeWindow(images[i][0], w, h)
        else:
            cv2.namedWindow("Image {} from {}".format(i+1, title), cv2.WINDOW_KEEPRATIO)
            cv2.imshow("Image {} from {}".format(i+1, title), images[i])
            cv2.resizeWindow("Image {} from {}".format(i+1, title), w, h)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def save(images, format, folder):
    for i in range(1, len(images)):
        path = "img/{}/{}_{}.{}".format(folder, folder, images[i][0], format)
        cv2.imwrite(path, images[i][1])

def save_set(images, keyword, format, folder):
    for i in range(len(images)):
        title = os.listdir(folder)[i]
        path = "{}/{}_{}".format(folder, keyword, title)
        cv2.imwrite(path, images[i])

# FILTER

def sharpen(img):
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    return cv2.filter2D(img, -1, kernel)

def blur(img, x):
    kernel = np.ones((x, x)) / x ** 2
    return cv2.filter2D(img, -1, kernel)

def filter_custom(img, kernel):
    kernel = np.array(kernel)
    return cv2.filter2D(img, -1, kernel)

# FEATURE

def match_keypoints(set, descriptors, keypoints, amount_matches=None, threshold=None):
    bf = cv2.BFMatcher(cv2.NORM_L1, crossCheck=True)

    matches = bf.match(descriptors[0], descriptors[1])
    matches = sorted(matches, key=lambda x: x.distance)

    matched = None
    if threshold:
        amount_keypoints = len(keypoints[0]) if len(keypoints[0])<len(keypoints[1]) else len(keypoints[1])
        match_percentage = len(matches) / amount_keypoints
        matched = True if match_percentage >= threshold else False
        print("\n\nThe two picture {}. ({}%)".format("match" if matched else "dont match", round(match_percentage*100),2))
    else:
        img = cv2.drawMatches(set[0], keypoints[0], set[1], keypoints[1], matches[:amount_matches], set[1], flags=2)
        plt.imshow(img)
        plt.show()

    return matches

def to_sift(set):
    sift_images = []
    descriptors = []
    keypoints = []

    for i in range(len(set)):
        siftobject = cv2.SIFT_create()
        keypoint, descriptor = siftobject.detectAndCompute(set[i], None)
        gray_scale = cv2.cvtColor(set[i], cv2.COLOR_BGR2GRAY)

        sift_images.append(cv2.drawKeypoints(gray_scale, keypoint, None))
        descriptors.append(descriptor)
        keypoints.append(keypoint)

    return sift_images, descriptors, keypoints

def print_keypoints(set_name, keypoints):
    print("\nKeypoints in {}:".format(set_name))
    i=0
    for amount in keypoints:
        i += 1
        print("  {} keypoints in image {}".format(len(amount), i))

def print_matches(set_name, matches):
    print("\n{} matches in {}".format(len(matches), set_name))


def apply_kernel(img, kernel):
    result = copy.deepcopy(img)
    for y in range(len(kernel)):
        for x in range(len(kernel)):
            v = 0
            for a in range(len(kernel)):
                for b in range(len(kernel)):

                    k = kernel[a][b]
                    d = len(kernel)//2
                    y1, x1 = y-d+a, x-d+b
                    if x1>=0 and x1<=len(img)-1 and y1>=0 and y1<=len(img)-1:
                        v += img[y1][x1]*k
                    else:
                        0 # zero-padding

            result[y][x] = v

    return result

if __name__ == '__main__':
    i = np.ones((3,3))
    k = np.eye(3)
    r = apply_kernel(i, k)
    print(r)