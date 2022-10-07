import time
import pyautogui
import pyperclip
import keyboard
from color import Color
from PIL.ImageGrab import grab


class Macro:
    def __init__(self):
        self.isPaused = False
        keyboard.add_hotkey("ctrl+r", self.pauseResume, timeout=999999)

    def pauseResume(self):
        if self.isPaused:
            self.isPaused = False
        else:
            self.isPaused = True

    def delay(self, millisecond: int):
        while self.isPaused:
            print("paused")
            time.sleep(1)

        if millisecond > 0:
            time.sleep(millisecond / 1000)

    def press(self, key: str, delay: int = 0):
        pyautogui.press(key)
        self.delay(delay)

    def keyDown(self, key: str, delay: int = 0):
        pyautogui.keyDown(key)
        self.delay(delay)

    def keyUp(self, key: str, delay: int = 0):
        pyautogui.keyUp(key)
        self.delay(delay)

    def write(self, str: str, delay: int = 0):
        pyautogui.write(str)
        self.delay(delay)

    def writePaste(self, str: str, delay: int = 0):
        pyperclip.copy(str)
        pyautogui.hotkey("ctrl", "v")
        self.delay(delay)

    def click(self, x: int, y: int, delay: int = 0):
        pyautogui.click(x, y)
        self.delay(delay)

    def ifColor(self, x: int, y: int, color: str):
        rgb = grab().load()[x, y]
        return "#" + color == Color.rgb2hex(rgb)

