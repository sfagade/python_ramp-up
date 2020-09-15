import cv2
import glob
from pathlib import Path

images = glob.glob("sample_images/*.jpg")

for image in images:
    img = cv2.imread(image, 1)
    re = cv2.resize(img, (100, 100))
    image_name = Path(image).name
    cv2.imshow("Hey "+image_name, re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_" + image_name, re)
