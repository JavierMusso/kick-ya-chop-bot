import cv2
import numpy as np
from PIL import ImageGrab
import win32gui



class Screenshots:

    # defining empty variables
    hwnd = None
    position = ()
    window_topleft = ()
    right = ()
    left = ()
    window = ()

    # constructor
    def __init__(self, window_name):
        # getting window name and window position.
        self.hwnd = win32gui.FindWindow(None, window_name)
        if not self.hwnd:
            raise Exception('Window not found: %s' % window_name)
        self.position = win32gui.GetWindowRect(self.hwnd)
        self.window_topleft = (self.position[0] + 608 , self.position[1] + 111)
        self.right = (self.window_topleft[0] + 470, self.window_topleft[1] + 540, self.window_topleft[0] + 471, self.window_topleft[1] + 542)
        self.left = (self.window_topleft[0] + 280, self.window_topleft[1] + 540, self.window_topleft[0] + 281, self.window_topleft[1] + 542)
        self.window = (self.window_topleft[0], self.window_topleft[1], self.window_topleft[0] + 703, self.window_topleft[1] + 937)

    # helper function, takes screenshots at the positions inputed
    def take_screenshot(self, pos): 
        screenshot = ImageGrab.grab(pos)
        screenshot = np.array(screenshot)
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2BGR)

        return screenshot

    # Specifies the screenshot area
    def get_screenshot(self, argument = 'window'):
        # window = window screen.
        # right = only the cards area. used to check if and what cards are there.
        # left = checks enemy hp, in order first to last.
        if (argument == 'right'):
            return self.take_screenshot(self.right)
        elif (argument == 'left'):
            return self.take_screenshot(self.left)
        else:
            return self.take_screenshot(self.window)
