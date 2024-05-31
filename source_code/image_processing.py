import cv2
from PyQt5.QtGui import QPixmap, QImage, QColor
from matplotlib import pyplot as plt
from source_code.resizeimg import resize_image
import numpy as np
def apply_contrast(self):
    clip_hist_percent = 20
    gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_size = len(hist)
    accumulator = [float(hist[0].item())]
    for index in range(1, hist_size):
        accumulator.append(accumulator[index - 1] + float(hist[index].item()))
    maximum = accumulator[-1]
    clip_hist_percent *= (maximum / 100.0)
    clip_hist_percent /= 2.0
    minimum_gray = 0
    while accumulator[minimum_gray] < clip_hist_percent:
        minimum_gray += 1
    maximum_gray = hist_size - 1
    while accumulator[maximum_gray] >= (maximum - clip_hist_percent):
        maximum_gray -= 1
    alpha = 255 / (maximum_gray - minimum_gray)
    beta = -minimum_gray * alpha
    contrast_img = cv2.convertScaleAbs(self.img, alpha=alpha, beta=beta)
    cv2.imwrite("test.jpg",contrast_img)
    self.img_path_editting = "test.jpg"
    self.ui.contrast_label.setPixmap(QPixmap("test.jpg"))

def show_histogram(self, img_path):
    if img_path:
        image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        plt.figure("Histogram")
        plt.hist(image.ravel(), 256, [0, 256])
        plt.title("Histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.show()
def adjust_color(self, hue, saturation, brightness):
    img = self.img.copy()
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    hsv[:, :, 0] = np.clip(hsv[:, :, 0] + hue, 0, 179)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] + saturation, 0, 255)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] + brightness, 0, 255)

    color_adjusted_img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    cv2.imwrite("test.jpg",color_adjusted_img)
    self.img_path_editting ='test.jpg'

    self.ui.color_label.setPixmap(QPixmap("test.jpg"))