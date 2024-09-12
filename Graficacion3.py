import cv2
import numpy as np

'''
print(cv2.__version__)
'''

frame = np.full((480, 640, 3), (255, 255, 255), dtype=np.uint8)
color = (0, 0, 0)

frame[100, 100] = color
frame[100, 101] = color
frame[101, 100] = color
frame[101, 101] = color

cv2.imshow("Frame con un Píxel Modificado", frame)

cv2.waitKey(0)
cv2.destroyAllWindows()