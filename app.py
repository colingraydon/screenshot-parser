import tkinter as tk
from tkinter import NW, filedialog, Text, Label
import pyautogui
import pytesseract


root = tk.Tk()


#can change background color here
canvas = tk.Canvas(root, height=400, width = 400, bg = "#222222")
canvas.pack()

# #creates the grid for times
# lbl = Label(root, text="hello world")
# lbl.grid(row=0, column=0)
# lbl.pack()

def take_screenshot():

    screenshot = pyautogui.screenshot()

    #setting points for cropping timer
    #this should work on any size monitor
    width, height = screenshot.size
    timer_left = (width / 2) - 50
    timer_right = (width / 2) + 50
    timer_top = 50
    timer_bot = 350

    screenshot_cropped = screenshot.crop((timer_left, timer_top, timer_right, timer_bot))

    #these lines will save the screenshot if needed later
    # save_path = filedialog.asksaveasfilename()
    # screenshot_cropped.save(save_path+"screenshottest.png")

    #these lines would put the screenshot onto the canvas
    # tk_image = tk.PhotoImage(screenshot_cropped)
    # canvas.create_image(10,10, image=tk_image, anchor=tk.NW)

    text = pytesseract.image_to_string(screenshot_cropped)
    print(text)
    #return text

def roshan():

    s = take_screenshot
    res = s + "Roshan"
    add_text(res)

def buyback():

    s = take_screenshot
    res = s + "Buyback"
    add_text(res)

def add_text(s):

    canvas.create_text(text=s, fill="white")

roshTimer = tk.Button(root, text="Rosh", command = take_screenshot, padx=10, pady=5 , fg="#222222")
roshTimer.pack(side = "left", anchor="e", expand=True)
buyback = tk.Button(root, text="Buyback", command = take_screenshot, padx=10, pady=5 , fg="#222222")
buyback.pack(side="left", anchor="w", expand=True)
clear = tk.Button(root, text="Clear", command = take_screenshot, padx=10, pady=5 , fg="#222222")
clear.pack(side="left", anchor="w", expand=True)

root.mainloop()
