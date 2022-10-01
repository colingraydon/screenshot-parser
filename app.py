import tkinter as tk
from tkinter import filedialog, Text
import numpy as np
import pyautogui
import pygetwindow
import pytesseract
from PIL import Image
import cv2
import os
from mss import mss

root = tk.Tk()


#can change background color here
canvas = tk.Canvas(root, height=600, width = 800, bg="#263D42")
canvas.pack()


def take_screenshot():

    screenshot = pyautogui.screenshot()
    titles = pygetwindow.getAllTitles()
    window = pygetwindow.getWindowsWithTitle("Dota2")[0]
    left, top = window.topleft
    right, bottom = window.bottomright


roshTimer = tk.Button(root, text="Rosh Timer", command = take_screenshot, padx=10, pady=5,  fg="white", bg="#263D42")
roshTimer.pack()

root.mainloop()
