import cv2

face_cascade = cv2.CascadeClassifier("Files/haarcascade_frontalface_default.xml")

img = cv2.imread("Photos/IMG-20200501-WA0013.jpg")
# img = cv2.resize(img, (int(img.shape[1]/6), int(img.shape[0]/6)))
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=2, minSize=(30, 30),
                                      flags=cv2.CASCADE_SCALE_IMAGE)

print(faces)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

resized = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))

cv2.imshow("Gray", resized)
cv2.waitKey(5000)
cv2.destroyAllWindows()
