import cv2
from PyQt5.QtGui import QPixmap, QImage
import numpy as np

def conllage(self,img,conllage_link):
    # Đọc hai hình ảnh
    img1 = cv2.imread(self.img_path)
    img2 = cv2.imread(conllage_link)

    # Kiểm tra kích thước hình ảnh
    print(f'Image 1 shape: {img1.shape}')
    print(f'Image 2 shape: {img2.shape}')

    # Thay đổi kích thước hình ảnh cho khớp nhau nếu cần thiết
    height1, width1 = img1.shape[:2]
    height2, width2 = img2.shape[:2]

    # Thay đổi kích thước hình ảnh thứ hai theo kích thước của hình ảnh thứ nhất
    img2_resized = cv2.resize(img2, (width1, height1))

    # Ghép hai ảnh theo chiều ngang
    horizontal_concat = np.hstack((img1, img2_resized))

    
    cv2.imwrite('test.jpg', horizontal_concat)
    self.ui.collage_label.setPixmap(QPixmap("test.jpg"))
