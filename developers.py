from tkinter import*
from tkinter import ttk # for stylish
from tkinter import messagebox

from PIL import Image, ImageTk  # for image
import os   # for photos
import csv
from tkinter import filedialog


class Developers:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x798+0+0")
        # self.root.geometry("1600x800+0+0")
        root.state('zoomed')
        self.root.title("Developers")
        # root.resizable(False, False)
        self.root.wm_iconbitmap("faceIcon.ico")
                
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

        # inserting the 1nd image
        top_img = Image.open(r"Pictures\Ali.jpg")
        top_img = top_img.resize((int(screen_width), int(screen_height) - 50), Image.LANCZOS)    # convert high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x = 0, y = 0, width = int(screen_width), height = int(screen_height) - 50)

if __name__ == "__main__":
    root = Tk() 
    obj = Developers(root)
    root.mainloop()