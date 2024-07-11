import cv2
import numpy as np

drawing = False
ix, iy = -1, -1
img = None
img_copy = None

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, img, img_copy

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        remove_object(ix, iy, x, y)

def remove_object(x1, y1, x2, y2):
    global img
    
    mask = np.zeros(img.shape[:2], np.uint8)
    cv2.rectangle(mask, (x1, y1), (x2,y2), (255, 255, 255), -1)
    
    result = cv2.inpaint(img, mask, 3, cv2.INPAINT_TELEA)
    
    cv2.imshow('Result', result)


def initialize_image(image_path):
    global img, img_copy
    img = cv2.imread(image_path)
    img_copy = img.copy()

def setup_window():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_rectangle)

def process_image():
    global img_copy
    while True:
        cv2.imshow('image', img_copy)
        k = cv2.waitKey(1) & 0xFF
        if k == 27:  # Nhấn 'ESC' để thoát
            break
    cv2.destroyAllWindows()