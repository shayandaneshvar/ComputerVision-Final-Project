import cv2
import numpy as np

from ImageTools import ImageProcessor
from VideoTools import VideoProcessor


def find_points_by_hand():
    def on_mouse(k, x, y, s, p):
        print(np.array([[np.float32(x)], [np.float32(y)]]))

    I2 = cv2.imread("images/2D_field.png")
    print(I2.shape)
    cv2.imshow("x", I2)
    cv2.setMouseCallback("x", on_mouse)
    cv2.waitKey()


if __name__ == '__main__':
    # find_points_by_hand()
    vp = VideoProcessor("videos/output.mp4")
    homography = ImageProcessor.get_perspective_transform()
    itr = vp.get_iterator()
    while itr.has_more():
        I = itr.get_next()
        if I is None:
            break
        G = cv2.warpPerspective(I, homography, (1000, 1000))
        cv2.imshow("sd", G)
        cv2.imshow("sdas", I)
        cv2.waitKey(15)
