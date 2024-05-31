from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget, QFileDialog
from PyQt5.QtGui import QPixmap, QPainter, QPen,QImage
from PyQt5.QtCore import Qt, QRect
import cv2
from modules.file_handling import load_image
import numpy as np
class CropWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        self.original_label = QLabel()
        imgcut = QFileDialog.getOpenFileName(filter='*.jpg *.jpeg *.png')
        img_path = imgcut[0]
        self.pixmap = QPixmap(img_path)
        self.original_label.setPixmap(self.pixmap)
        self.original_label.mousePressEvent = self.start_crop
        self.original_label.mouseMoveEvent = self.update_crop
        self.original_label.mouseReleaseEvent = self.end_crop
        self.cropped_label = QLabel()
        layout.addWidget(self.original_label)
        layout.addWidget(self.cropped_label)
        self.setLayout(layout)
        self.crop_start = None
        self.crop_end = None

    def start_crop(self, event):
        self.crop_start = event.pos()

    def update_crop(self, event):
        if self.crop_start is not None:
            self.crop_end = event.pos()
            self.update()

    def end_crop(self, event):
        self.crop_end = event.pos()
        self.update()
        self.save_cropped_image()

    def paintEvent(self, event):
        painter = QPainter(self.original_label.pixmap())
        painter.drawPixmap(self.rect(), self.pixmap)
        if self.crop_start and self.crop_end:
            painter.setPen(QPen(Qt.red, 3, Qt.SolidLine))
            crop_rect = QRect(self.crop_start, self.crop_end)
            painter.drawRect(crop_rect)
        painter.end()
        self.original_label.setPixmap(self.original_label.pixmap())

    def save_cropped_image(self):
        def qpixmap_to_nparray(qpixmap):
            # Chuyển đổi QPixmap thành QImage
            qimage = qpixmap.toImage()
            width = qimage.width()
            height = qimage.height()
            bytes_per_line = qimage.bytesPerLine()
            channels_count = qimage.depth() // 8
            format_ = qimage.format()

            # Đảm bảo ảnh có định dạng RGB
            if format_ != QImage.Format_RGB32:
                qimage = qimage.convertToFormat(QImage.Format_RGB32)

            # Tạo một bộ đệm để lưu trữ dữ liệu ảnh
            ptr = qimage.constBits()
            ptr.setsize(qimage.byteCount())
            arr = np.array(ptr).reshape(height, width, channels_count)
            
            # Chuyển đổi RGB thành BGR (nếu cần, vì OpenCV sử dụng định dạng BGR)
            return arr[:, :, ::-1].copy()
        
        if self.crop_start and self.crop_end:
            crop_rect = QRect(self.crop_start, self.crop_end)
            cropped_pixmap = self.pixmap.copy(crop_rect)
            cropped_image = qpixmap_to_nparray(cropped_pixmap)
            cv2.imwrite("test.jpg",cropped_image)
    
        