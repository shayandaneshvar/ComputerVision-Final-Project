import cv2
import numpy as np


class ImageProcessor:
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def get_perspective_transform():
        points1 = np.array([[873, 779],
                            [693, 253],
                            [660, 163],
                            [640, 110],
                            [142, 167],
                            [1141, 116],
                            [37, 209],
                            [1259, 144]], dtype=np.float32)
        points2 = np.array([[499, 600],
                            [499, 406],
                            [499, 265],
                            [499, 71],
                            [218, 178],
                            [781, 179],
                            [218, 280],
                            [781, 280]], dtype=np.float32)
        homography, mask = cv2.findHomography(points1, points2)
        # print(mask)
        print(homography)
        return homography
