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
def clickLeftCur():#单击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
 
def moveCurPos(x,y):#移动鼠标
    windll.user32.SetCursorPos(x, y)
    print ("moveto :%s :%s",x,y)
 
def getCurPos():#获得鼠标位置信息，这个再实际代码没用上，调试用得上
    return win32gui.GetCursorPos()


def window_capture(filename):
    hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # 获取监控器信息
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)
 
 
def get_screen():
    try:
        time.sleep(3)
        window_capture("F:/YYS/background.png")
    except:
        print ("catch screen error!!!!!")
    img = cv2.imread("F:/YYS/background.png",0)
    return img
 
def match(img1, template):
    """img1代表待匹配图像, img2代表模板"""
    res = cv2.matchTemplate(img1,template,cv2.TM_CCOEFF_NORMED)
    maxres = res.max()
    print ("maxres%s"%maxres)
    return maxres
 
def get_randxy(x, y):
    """产生一个在x,y二维区域内的随机位置,x,y为两个元素的列表，变量范围"""
    xc = random.randint(x[0], x[1])
    yc = random.randint(y[0], y[1])
 
    return xc,yc
 
def get_randtime(a, b):
    """产生a,b间的随机时间延迟"""
    time.sleep(random.uniform(a, b))
 
def click(x, y):
    """输入两个二维列表，表示要点击的位置的x坐标，y坐标"""
    moveCurPos(x,y)
    clickLeftCur()
    clickLeftCur()

# time.sleep(2)
# for a in range(10):
#     moveCurPos(111,a+222)
#    clickLeftCur()