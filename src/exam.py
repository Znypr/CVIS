import copy

import numpy as np
from numpy import median


def convert_kernel_to_binary (img, t):
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


def apply_kernel_to_img (img, kernel, coef):
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
    return np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])


def project_point (p, P):
    return P.dot(p)


def homogenous_to_kartesian (p):
    k = []
    for dim in p:
        k.append(dim / p[len(p) - 1])
    k.pop()
    return k


def point_in_canvas (p, canvas):
    return p[0] <= canvas[0] and p[1] <= canvas[1]


if __name__ == '__main__':

    img = [[10, 4, 3], [4, 6, 1], [1, 1, 8]]
    kernel = np.ones((3, 3))
    coefficient = 1 / 9
    threshold = 5

    canvas = (640, 240)
    fx, fy = 10, 10
    cx, cy = 20, 20
    K = get_calibrationmatrix(fx, fy, cx, cy)

    R = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    t = np.array([[1], [2], [3]])

    P = get_projection_matrix(K, R, t)

    point = np.array([1, 1, 1, 1])

    # Bild mit Maske filtern (RETURN: filtered img)
    r1 = apply_kernel_to_img(img, kernel, coefficient)

    # Binärbild bestimmen (RETURN: Binärbild)
    r2 = convert_kernel_to_binary(img, threshold)

    # Maske auf Summe 1 prüfen (RETURN: boolean)
    r3 = kernel_is_normalized(img, coefficient)

    # Hauptpixel nach Median filtern (RETURN: img, median)
    r4, r5 = filter_median(img)

    # Bestimme Projektionsmatrix
    r6 = get_projection_matrix(K, R, t)

    # homogenen Punkt projektieren
    r7 = project_point(point, P)

    # kartesischen Punkt bestimmen
    r8 = homogenous_to_kartesian(r7)

    # liegt Punkt im Bild?
    r9 = point_in_canvas(r8, canvas)

    print(r9)
