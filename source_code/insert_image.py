import cv2
from PyQt5.QtGui import QPixmap, QImage
import numpy as np


def insert_image(self, img, insert_img_path, x, y):
    insert_img = cv2.imread(insert_img_path, cv2.IMREAD_GRAYSCALE)
    background_img = cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)

    insert_height, insert_width = insert_img.shape
    rows, cols = background_img.shape

    if y + insert_height > rows or x + insert_width > cols:
        raise ValueError("The object exceeds the boundaries of the background image")

    roi = background_img[y:y + insert_height, x:x + insert_width]
    roi = insert_img  # Replace the ROI with the grayscale insert image

    # Place the modified ROI back into the original image
    background_img[y:y + insert_height, x:x + insert_width] = roi

    # Save the modified image
    cv2.imwrite("test.jpg", background_img)

    # Update instance variables or UI elements
    self.img_path_editing = "test.jpg"
    self.ui.insertimg_label.setPixmap(QPixmap("test.jpg"))
