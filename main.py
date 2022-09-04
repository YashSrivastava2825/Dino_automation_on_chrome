import pyautogui
from PIL import Image, ImageGrab
import time


def hit(key):
    pyautogui.keyDown(key)

def isCollide(data):
    for i in range(250, 355):
        for j in range(525, 555):
            if data[i, j] > 100:
                hit("down")
                return
    for i in range(300, 436):
        for j in range(567, 650):
            if data[i, j] > 100:
                hit("up")
                return
    return


if __name__ == "__main__":
    print("Hey ... Dino game is about to start in 3 seconds")
    time.sleep(3)
    hit("up")

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)


