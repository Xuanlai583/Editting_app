# resize_func.py
import cv2
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QMessageBox

def resize_image(self, new_width, new_height, img ):
    if self.img_path:
        valid_input = False
        while not valid_input:
            try:
                # Kiểm tra giá trị width và height
                if new_width <= 0 or new_height <= 0:
                    raise ValueError("Giá trị chiều rộng và chiều cao phải lớn hơn 0.")

                valid_input = True

            except ValueError as e:
                reply = QMessageBox.warning(self, "Lỗi", str(e), QMessageBox.Retry | QMessageBox.Cancel)

                if reply == QMessageBox.Cancel:
                    return

    # Resize the image
    resized_image = cv2.resize(img, (new_width, new_height), interpolation= cv2.INTER_NEAREST)
    cv2.imwrite("test.jpg",resized_image)
    self.img_path_editting = "test.jpg"
    # Convert the resized image to QPixmap for display
    # qpixmap = QPixmap.fromImage(QImage(resized_image.data, resized_image.shape[1], resized_image.shape[0], QImage.Format_RGB888))
    # Display the resized image
    self.ui.resize_label.setPixmap(QPixmap("test.jpg"))