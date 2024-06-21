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
#ap dung keo dan tuyen tinh    
def contrast2(self):
    image = cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)

    min_val = np.min(image)
    max_val = np.max(image)

    stretched_image = ((image - min_val)/(max_val - min_val)* 255).astype(np.uint8)

    cv2.imwrite("test.jpg", stretched_image)
    self.img_path_editting = "test.jpg"
    self.ui.contrast_label.setPixmap(QPixmap("test.jpg"))
def contrast3(self):
    image =cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)

    equalizer_img = cv2.equalizeHist(image)

    cv2.imwrite("test.jpg", equalizer_img)
    self.img_path_editting = "test.jpg"
    self.ui.contrast_label.setPixmap(QPixmap("test.jpg"))
def contrast4(self):
    import cv2
    import numpy as np
    from PyQt5.QtGui import QPixmap

    # Đọc ảnh ở dạng grayscale
    image = cv2.imread(self.img_path, cv2.IMREAD_GRAYSCALE)
    
    # Đảm bảo ảnh được tải thành công
    if image is None:
        raise FileNotFoundError(f"Không tìm thấy ảnh tại {self.img_path}")

    # Chuẩn hóa giá trị pixel về khoảng [0, 1]
    normalized_image = image / 255.0

    # Tính hằng số log transform c
    c = 255 / np.log(1 + np.max(normalized_image))

    # Áp dụng phép biến đổi log
    log_transformed_image = c * np.log1p(normalized_image)

    # Chuẩn hóa lại về khoảng [0, 255] và chuyển sang uint8
    log_transformed_image = np.uint8(log_transformed_image * 255)

    # Lưu ảnh đã biến đổi
    cv2.imwrite("test.jpg", log_transformed_image)
    
    # Cập nhật đường dẫn ảnh đã chỉnh sửa
    self.img_path_editting = "test.jpg"
    
    # Cập nhật giao diện người dùng với ảnh mới
    self.ui.contrast_label.setPixmap(QPixmap("test.jpg"))

