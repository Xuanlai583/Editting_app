import cv2
import numpy as np

class ImageCropper:
    def __init__(self, img_path):
        self.image = cv2.imread(img_path)
        self.original_image = self.image.copy()
        self.start_point = None
        self.end_point = None
        self.drawing = False

    def mouse_callback(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.start_point = (x, y)
            self.drawing = True
        elif event == cv2.EVENT_MOUSEMOVE:
            if self.drawing:
                self.end_point = (x, y)
        elif event == cv2.EVENT_LBUTTONUP:
            self.end_point = (x, y)
            self.drawing = False

    def crop_image(self):
        cv2.namedWindow('Select Region to Crop')
        cv2.setMouseCallback('Select Region to Crop', self.mouse_callback)

        while True:
            clone = self.image.copy()

            if self.start_point and self.end_point:
                cv2.rectangle(clone, self.start_point, self.end_point, (0, 255, 0), 2)

            cv2.imshow('Select Region to Crop', clone)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('r'):  # Press 'r' to reset selection
                self.image = self.original_image.copy()
                self.start_point = None
                self.end_point = None
            elif key == ord('c'):  # Press 'c' to crop
                if self.start_point and self.end_point:
                    x1, y1 = self.start_point
                    x2, y2 = self.end_point
                    x = min(x1, x2)
                    y = min(y1, y2)
                    width = abs(x2 - x1)
                    height = abs(y2 - y1)

                    cropped_image = self.original_image[y:y+height, x:x+width]
                    cv2.destroyAllWindows()
                    return cropped_image
            elif key == 27:  # Press Esc to exit
                cv2.destroyAllWindows()
                return None

if __name__ == "__main__":
    img_path = "your_image.jpg"  # Replace with your image path
    cropper = ImageCropper(img_path)
    cropped_image = cropper.crop_image()

    if cropped_image is not None:
        cv2.imwrite("cropped_image.jpg", cropped_image)
        self.ui.resize_label.setPixmap(QPixmap("test.jpg"))
        print("Cropped image saved as 'cropped_image.jpg'")
    else:
        print("No region selected for cropping")
