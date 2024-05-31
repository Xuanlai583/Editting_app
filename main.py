import sys
from PyQt5 import QtCore,QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream
from PyQt5.QtGui import QPixmap,QPainter,QPen
from PyQt5.QtWidgets import *
import cv2
from matplotlib import pyplot as plt
from PIL import Image, ImageTk
import numpy as np

from modules.navigation import setup_navigation
from source_code.resizeimg import resize_image
from modules.file_handling import load_image
from source_code.image_processing import apply_contrast, show_histogram, adjust_color
from source_code.insert_image import insert_image
from source_code.crop import CropWindow
from ui.interface_demo import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.img = None
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.new_width_input = self.ui.new_width
        self.ui.new_height_input = self.ui.new_height
        self.ui.new_width_insert = self.ui.insert_width
        self.ui.new_height_insert = self.ui.insert_height
        self.ui.icon_only_frame.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.file_btn.setChecked(True)

        self.ui.Resize_btn_full.clicked.connect(self.resize_image)
        self.ui.file_btn_full.clicked.connect(self.load_image)
        self.ui.Histogram_btn_full.clicked.connect(self.show_histogram)
        self.ui.Contrast_btn_full.clicked.connect(self.apply_contrast)
        self.ui.Color_btn_full.clicked.connect(self.apply_color)
        self.ui.insertimg_btn_full.clicked.connect(self.insert_object)
        self.ui.Cut_btn_full.clicked.connect(self.crop_image)

         # Connect color adjustment sliders to the function
        self.ui.hue_slider.valueChanged.connect(self.update_color)
        self.ui.saturation_slider.valueChanged.connect(self.update_color)
        self.ui.brightness_slider.valueChanged.connect(self.update_color)

        setup_navigation(self.ui)

        self.img_path = None
        self.img_path_editting = None
        self.crop_start = None
        self.crop_end = None

    def resize_image(self):
        new_width = int(self.ui.new_width_input.text())
        new_height = int(self.ui.new_height_input.text())
        resize_image(self, new_width, new_height, self.img)

    def load_image(self):
        self.img_path, self.img = load_image(self)
        if self.img_path:
            self.ui.file_label.setPixmap(QPixmap(self.img_path))
            self.ui.stackedWidget.setCurrentWidget(self.ui.page)

    def apply_contrast(self):
        apply_contrast(self)

    def show_histogram(self):
        show_histogram(self, self.img_path_editting)

    def apply_color(self):
        hue = self.ui.hue_slider.value()
        saturation = self.ui.saturation_slider.value()
        brightness = self.ui.brightness_slider.value()
        adjust_color(self, hue, saturation, brightness)

    def update_color(self):
        if self.img is not None:
            self.apply_color()

    def insert_object(self):
        insert_height = int(self.ui.insert_height.text())
        insert_width = int(self.ui.insert_width.text())
        object_img = QFileDialog.getOpenFileName(filter='*.jpg *.jpeg *.png')
        object_path = object_img[0]
        insert_image(self,self.img,object_path,insert_height,insert_width)

    def crop_image(self):
                self.setWindowTitle("Crop Image")
                self.crop_window = CropWindow(self)
                self.setCentralWidget(self.crop_window)
                self.ui.cut_label.setPixmap(QPixmap("test.jpg"))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_file = QFile("resources/style.qss")
    style_file.open(QFile.ReadOnly | QFile.Text)
    style_stream = QTextStream(style_file)
    app.setStyleSheet(style_stream.readAll())

    window = MainWindow()
    window.show()
    sys.exit(app.exec())