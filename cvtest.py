# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 23:43:38 2019

@author: jiangsheng
"""

import pyautogui
import ctypes
import os
import cv2
import random
import time
import win32gui
import win32ui
import win32api
import win32con
from ctypes import *

t_start = cv2.imread('F:/YYS/beforeend.png', 0)
img = cv2.imread("F:/YYS/test4.png", 0)
res = cv2.matchTemplate(img, t_start, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
corner_loc = (max_loc[0] + 50, max_loc[1] + 150)
player_spot = (max_loc[0] + 25, max_loc[1] + 150)
cv2.circle(img, player_spot, 10, (0, 255, 255), -1)
cv2.rectangle(img, max_loc, corner_loc, (0, 0, 255), 5)
cv2.namedWindow('img', cv2.WINDOW_KEEPRATIO)
cv2.imshow("img", img)
cv2.waitKey(0)
maxres = res.max()
print("maxres%s" % maxres)