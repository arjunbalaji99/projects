import pyautogui
from numpy import *
import time
from PIL import ImageGrab, ImageOps


class Cordinates():
    replayBtn = (564, 630)
    dino = (215, 638)

def restart():
    pyautogui.click(Cordinates.replayBtn)


def pressspace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def imagegrab():
    box = (Cordinates.dino[0] + 60, Cordinates.dino[1], Cordinates.dino[0] + 100, Cordinates.dino[1] + 30)
    image = ImageGrab.grab(box)
    grey = ImageOps.grayscale(image)
    a = array(grey.getcolors())
    return a.sum()


def main():
    restart()
    while True:
        if imagegrab() != 1447:
            pressspace()
            time.sleep(0.1)


main()