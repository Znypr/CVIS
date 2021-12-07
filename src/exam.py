import copy

import numpy as np
from numpy import median


def convert_img_to_binary (img, t):
    for x in range(len(img)):
        for y in range(len(img)):
            if img[y][x] >= t:
                img[y][x] = 255
            else:
                img[y][x] = 0
    return img


def kernel_is_normalized (kernel, coef = 1.):
    sum = 0
    for col in kernel:
        for val in col:
            sum += val

    return sum * coef == 1


def apply_kernel_to_img (img, kernel, coef = 1):
    result = copy.deepcopy(img)
    for y in range(len(kernel)):
        for x in range(len(kernel)):
            v = 0
            for a in range(len(kernel)):
                for b in range(len(kernel)):

                    k = kernel[a][b]
                    d = len(kernel) // 2
                    y1, x1 = y - d + a, x - d + b
                    if x1 >= 0 and x1 <= len(img) - 1 and y1 >= 0 \
                            and y1 <= len(img) - 1:
                        v += img[y1][x1] * k
                    else:
                        0  # zero-padding

            result[y][x] = v

    result = np.rint(np.array(result) * coef)
    return result


def filter_median (kernel):
    m = median(kernel)
    kernel[1][1] = median(kernel)
    return kernel, m


def get_projection_matrix (
        K, R = np.array(np.eye(3)),
        t = np.array(np.zeros((3, 1)))
):
    matrix = K.dot(R)
    return np.hstack((matrix, t))


def get_calibrationmatrix (fx, fy, cx, cy):
    return np.array(
        [[fx, 0, cx],
         [0, fy, cy],
         [0, 0, 1]]
    )


def project_point (p, P):
    return P.dot(p)


def homogenous_to_kartesian (p):
    k = []
    for dim in p:
        k.append(round(dim / p[len(p) - 1]))
    k.pop()
    return k


def point_in_canvas (p, canvas):
    return p[0] <= canvas[0] and p[1] <= canvas[1] \
           and p[0] >= 0 and p[1] >= 0


if __name__ == '__main__':

    # DEFINITIONS

    img = [[1, 4, 9], [2, 9, 1], [6, 1, 3]]
    mask = np.ones((3, 3))
    #mask = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
    coefficient = 1/9
    threshold = 5

    canvas = (640, 480)
    fx, fy = 460, 460
    cx, cy = 320, 240
    K = get_calibrationmatrix(fx, fy, cx, cy)

    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    t = np.array([[1], [2], [3]])

    P = get_projection_matrix(K, R, t)  # extrinsic relevant
    # P = get_projection_matrix(K)  # extrinsic irrelevant
    P = np.array(
        [[0, -510, 320, 1850], [520, 0, 240, 1280], [0, 0, 1,
                                                     1]]
    )

    point = np.array([2, 2, 2, 1])  # homogenous 3D point

    # FUNCTIONS CALL

    # Bild mit Maske filtern (RETURN: filtered img)
    r1 = apply_kernel_to_img(img, mask, coefficient)

    # Binärbild bestimmen (RETURN: Binärbild)
    r2 = convert_img_to_binary(img, threshold)

    # Maske auf Summe 1 prüfen (RETURN: boolean)
    r3 = kernel_is_normalized(img, coefficient)

    # Hauptpixel nach Median filtern (RETURN: img, median)
    r4, r5 = filter_median(img)

    # Bestimme Projektionsmatrix (RETURN: P)
    r6 = P

    # homogenen Punkt projektieren (RETURN: 2D-homogenous point)
    r7 = project_point(point, P)

    # kartesischen Punkt bestimmen (RETURN: 2D-kartesian point)
    r8 = homogenous_to_kartesian(r7)

    # liegt Punkt im Bild? (RETURN: boolean)
    r9 = point_in_canvas(r8, canvas)

    # RESULTS

    print(P, r7, r8, r9, "\n")
    print(r1, "\n")
