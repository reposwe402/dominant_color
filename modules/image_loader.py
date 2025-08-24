import cv2

def load_image(path):
    try:
        img = cv2.imread(path)
        cv2.imshow("img", img)
        return img
    except Exception:
        print("Path not found")
        exit()
