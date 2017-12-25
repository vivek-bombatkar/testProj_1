'''
from SimpleCV import Camera
import time

cam = Camera()
time.sleep(0.1)  # If you don't wait, the image will be dark
img = cam.getImage()
img.save("simplecv.png")

import pygame
import pygame.camera
import time

pygame.camera.init()
pygame.camera.list_cameras()
cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()
time.sleep(0.1)  # You might need something higher in the beginning
img = cam.get_image()
pygame.image.save(img, "pygame.jpg")
cam.stop()
'''

import cv2
camera = cv2.VideoCapture(0)
while True:
    return_value,image = camera.read()
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow('image',gray)
    if cv2.waitKey(1)& 0xFF == ord('s'):
        cv2.imwrite('test.jpg',image)
        break
camera.release()
cv2.destroyAllWindows()