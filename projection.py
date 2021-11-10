import cv2
import functions
import numpy as np
import copy

def mutiply_vector_matrix(point, P):
    projected_point = []

    for i in range(len(P)):
        dim_i = 0
        for j in range(len(P[0])):
            dim_i += P[i][j] * point[j]
        projected_point.append(dim_i)

    return projected_point

def get_homogenous_points(kartesic_points):

    homogenous_points = copy.deepcopy(kartesic_points)

    for point in homogenous_points:
        homogenous_point = point.append(1)

    return homogenous_points

def get_cameramatrix(fx, fy, cx, cy):

    return [[fx, 0, cx],
            [0, fy, cy],
            [0, 0, 1]]

def get_projection(K, R=None, t=(0, 0, 0)):
    P = copy.deepcopy(K)

    if R:
        0
    else:
        for i in range(len(P)):
            P[i].append(t[i])

    return P

def project(points, P):
    projected_points = []

    for point in points:
        p = mutiply_vector_matrix(point, P)
        projected_points.append(p)

    return projected_points

def compress_dimension(points_nd):
    # points_nd := points with n dimensions
    # pints_nminus1d := points with (n-1) dimensions

    points_nminus1d = []

    for point_nd in points_nd:
        point_nminus1d = []
        for i in range(len(point_nd)-1):
            point_nminus1d.append(point_nd[i]/point_nd[len(point_nd)-1])
        points_nminus1d.append(point_nminus1d)

    return points_nminus1d

def contains(points, canvas):
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
    p1 = [10, 10, 100]
    p2 = [33, 22, 111]
    p3 = [100, 100, 1000]
    p4 = [20,-100, 100]
    kartesic_points = [p1, p2, p3, p4]
    points = get_homogenous_points(kartesic_points)

    K = get_cameramatrix(fx, fy, cx, cy)
    P = get_projection(K)


    # TASK 1
    projected_points_3d = project(points, P)
    projected_points_2d = compress_dimension(projected_points_3d)

    print(projected_points_2d)
    print(contains(projected_points_2d, canvas))


    # TASK 2
    points = np.float32(kartesic_points)
    points = np.transpose(points)
    R, t= np.eye(3), np.zeros(3)
    K = np.float32(K)

    distCoeffs = None

    output = np.zeros((2,4))

    projected_points = cv2.projectPoints(points, R, t, K, distCoeffs)
    print(projected_points)
