import cv2
import numpy as np

# Đọc ảnh
img = cv2.imread('test.jpg')

# Tạo mask cho vùng cần xóa
mask = np.zeros(img.shape[:2], np.uint8)

# Chọn vùng cần xóa (ví dụ: hình chữ nhật)
rectangle = (50, 50, 100, 100)  # (x, y, width, height)
cv2.rectangle(mask, (rectangle[0], rectangle[1]), 
              (rectangle[0] + rectangle[2], rectangle[1] + rectangle[3]), 
              (255, 255, 255), -1)

# Áp dụng thuật toán inpainting
result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)

# Hiển thị kết quả
cv2.imshow('Original', img)
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Lưu ảnh kết quả
cv2.imwrite('output_image.jpg', result)