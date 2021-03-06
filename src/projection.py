import copy

import cv2
import numpy as np


def get_homogenous_points (kartesic_points):
    homogenous_points = copy.deepcopy(kartesic_points)

    for point in homogenous_points:
        homogenous_point = point.append(1)

    return homogenous_points


def get_cameramatrix (fx, fy, cx, cy):
    return [[fx, 0, cx], [0, fy, cy], [0, 0, 1]]


def get_projection (K, R = None, t = np.zeros((3,1))):

    if(R):
        P = K.dot(R)
        return np.hstack((P, t))
    else:
        return np.hstack((K, t))



def project (points, P):
    projected_points = []

    for point in points:
        p = P.dot(point)
        projected_points.append(p)

    return projected_points


def homogenous_to_cartesic (points_nd):
    # points_nd := points with n dimensions
    # pints_nminus1d := points with (n-1) dimensions

    points_nminus1d = []

    for point_nd in points_nd:
        point_nminus1d = []
        for i in range(len(point_nd) - 1):
            point_nminus1d.append(
                point_nd[i] / point_nd[len(point_nd) - 1]
            )
        points_nminus1d.append(point_nminus1d)

    return points_nminus1d


def contains (points, canvas):
    points_in_canvas = []

    for point in points:
        in_canvas = True
        for i in range(len(point)):
            if point[i] > canvas[i] or point[i] < 0:
                in_canvas = False
        points_in_canvas.append(in_canvas)

    return points_in_canvas


if __name__ == '__main__':

    # intrinsic
    fx, fy = 460, 460
    cx, cy = 320, 240
    x, y = 640, 480
    canvas = [x, y]

    # extrinsic
    ## world-/camera coordinate system identical
    ## => no rotation/translation

    # points
    p1 = [1, 2, 3]
    p2 = [2, 2, 2]  # rounding
    kartesic_points = [p1, p2]
    points = get_homogenous_points(kartesic_points)

    K = get_cameramatrix(fx, fy, cx, cy)
    P = get_projection(K)

    # TASK 1
    projected_points_3d = project(points, P)
    projected_points_2d = homogenous_to_cartesic(projected_points_3d)

    print(projected_points_2d)
    #print(contains(projected_points_2d, canvas))

    # TASK 2
    points = np.float32(kartesic_points)
    points = np.transpose(points)

    R, t = np.eye(3), np.zeros(3)
    K = np.float32(K)

    distCoeffs = None

    projected_points = cv2.projectPoints(points, R, t, K, distCoeffs)

    #print(projected_points)
