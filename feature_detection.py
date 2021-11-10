import cv2
import functions
import numpy as np

if __name__ == '__main__':

# step 1: read image set

    #set1 = functions.read_folder("img/sets/set1", 1)
    set2 = functions.read_folder("img/sets/set2", 1)
    #set3 = functions.read_folder("img/sets/set3", 1)


# step 2: extract keypoints, save images, print amount keypoints

    #sift_set1, descriptor1, keypoints1 = functions.to_sift(set1)
    sift_set2, descriptor2, keypoints2 = functions.to_sift(set2)
    #sift_set3, descriptor3, keypoints3 = functions.to_sift(set3)

    #functions.save_set(sift_set1, "sift", "png", "img/sets/set1")
    #functions.save_set(sift_set2, "sift", "png", "img/sets/set2")
    #functions.save_set(sift_set3, "sift", "jpg", "img/sets/set3")

    #functions.print_keypoints("set-1", keypoints1)
    #functions.print_keypoints("set-2", keypoints2)
    #functions.print_keypoints("set-3", keypoints3)

    #functions.show(set1, sift_set1, "set-1")
    #functions.show(set2, sift_set2, "set-2")
    #functions.show(set3, sift_set3, "set-3")


# step 3: matching (all; top 30 => amount_matches=30; t == 0.7 => threshold=0.7)

    #amount_matches1 = functions.match_keypoints(set1, descriptor1, keypoints1, amount_matches=30)
    #functions.print_matches("set-1", amount_matches1)

    amount_matches2 = functions.match_keypoints(set2, descriptor2, keypoints2)
    functions.print_matches("set-2", amount_matches2)

    #amount_matches3 = functions.match_keypoints(set3, descriptor3, keypoints3, amount_matches=30)
    #functions.print_matches("set-3", amount_matches3)

    #Threshold über cv2.KNN(2) => Threshold := zwei matches vergleichen, m1*0.7 >= m2 => m2




