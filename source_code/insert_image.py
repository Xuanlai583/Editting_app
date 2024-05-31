import cv2
from PyQt5.QtGui import QPixmap, QImage
import numpy as np

def insert_image(self, img, insert_img_path, x, y):
    insert_img = cv2.imread(insert_img_path,cv2.IMREAD_UNCHANGED)
    background_img = cv2.imread(self.img_path)


    insert_height, insert_width,insert_channels =insert_img.shape
    rows, cols, channel = background_img.shape

    if y + insert_height > rows or x + insert_width > cols:
        raise ValueError("The object exceeds the boundaries of the background image")

    alpha_channel = insert_img[:, :, 3]
    alpha_inv = cv2.bitwise_not(alpha_channel)

    object_rgb = insert_img[:, :, :3]

    roi = background_img[y:y + insert_height, x:x + insert_width]

    # Blend the object into the ROI
    bg_roi = cv2.bitwise_and(roi, roi, mask=alpha_inv)
    fg_roi = cv2.bitwise_and(object_rgb, object_rgb, mask=alpha_channel)
    combined = cv2.add(bg_roi, fg_roi)

    # Place the blended ROI back into the original image
    background_img[y:y + insert_height, x:x + insert_width] = combined
    # self.img[y:y+self.insert_img.shape[0], x:x+self.insert_img.shape[1]] = self.insert_img[:, :, :3]
    cv2.imwrite("test.jpg",background_img)
    self.img_path_editting = "test.jpg"
    self.ui.insertimg_label.setPixmap(QPixmap("test.jpg"))