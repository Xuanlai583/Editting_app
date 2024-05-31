from PyQt5.QtWidgets import QFileDialog
import cv2

def load_image(self):
    link = QFileDialog.getOpenFileName(filter='*.jpg *.jpeg *.png')
    img_path = link[0]
    if img_path:
        img = cv2.imread(img_path, 1)
        (h, w, d) = img.shape
        print("width={}, height={}, depth{}".format(w, h, d))
        img_path_editting = img_path
        return img_path, img
    return None, None
