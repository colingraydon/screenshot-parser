import tkinter as tk
from tkinter import NW, filedialog, Text
import numpy as np
import pyautogui
import pytesseract
from PIL import Image
import cv2
import os
from mss import mss

root = tk.Tk()


#can change background color here
canvas = tk.Canvas(root, height=600, width = 800, bg = "#2A403D")
canvas.pack()


def take_screenshot():

    screenshot = pyautogui.screenshot()

    #setting points for cropping timer
    width, height = screenshot.size
    timer_left = (width / 2) - 50
    timer_right = (width / 2) + 50
    timer_top = 50
    timer_bot = 150

    screenshot_cropped = screenshot.crop((timer_left, timer_top, timer_right, timer_bot))

    #these lines will save the screenshot if needed later
    # save_path = filedialog.asksaveasfilename()
    # screenshot_cropped.save(save_path+"screenshottest.png")

    tk_image = tk.PhotoImage(screenshot_cropped)
    canvas.create_image(10,10, image=tk_image, anchor=tk.NW)


roshTimer = tk.Button(root, text="Rosh Timer", command = take_screenshot, padx=10, pady=5,  fg="white")
roshTimer.pack()

root.mainloop()
