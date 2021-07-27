import numpy as np
import pyautogui as pag
import cv2
from time import time
from window_capture import WindowCapture


win_capture = WindowCapture('Аллоды Онлайн')

loop_time = time()
while True:
    image = win_capture.get_screenshot()

    cv2.imshow('test', image)

    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break