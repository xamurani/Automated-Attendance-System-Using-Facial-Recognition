from tkinter import*
from tkinter import ttk # for stylish
import tkinter
from PIL import Image, ImageTk  # for image
import os   # for photos
from tkinter import messagebox

from student import Student
from train import Train
from face_recongnition import Face_Recongition
from attendance import Attendance
from time import strftime
from datetime import datetime
from developers import Developers
from helpDesk import HelpDesk

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x798+0+0")
        self.root.geometry("1600x800+0+0")
        root.state('zoomed')
        self.root.title("Automated Attendance System Using Facial Recognition")
        self.root.wm_iconbitmap("faceIcon.ico")
        #root.resizable(False, False)

        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        thirdOfScreen_width = screen_width / 3;

        # inserting the 1st image
        img = Image.open(r"Pictures\third.jpg")
        img = img.resize((int(thirdOfScreen_width), 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x = 0, y = 0, width = int(thirdOfScreen_width), height = 130)

        # inserting the 2nd image
        img1 = Image.open(r"Pictures\second.jpg")
        img1 = img1.resize((int(thirdOfScreen_width), 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x = int(thirdOfScreen_width), y = 0, width = int(thirdOfScreen_width), height = 130)

        # inserting the 3rd image
        img2 = Image.open(r"Pictures\first.jpg")
        img2 = img2.resize((int(thirdOfScreen_width), 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x = int(thirdOfScreen_width) + int(thirdOfScreen_width), y = 0, width = int(thirdOfScreen_width), height = 130)

        # bg image
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        # self.root.geometry("{}x{}".format(screen_width, screen_height))
        img3 = Image.open(r"Pictures\background1.png")
        img3 = img3.resize((screen_width, screen_height), Image.LANCZOS)    # convert high level image to low level
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x = 0, y = 130, width = screen_width, height = screen_height)

        # title lable
        title_lbl = Label(bg_img, text = "AUTOMATED ATTENDANCE SYSTEM USING FACIAL RECOGNITION", font = ("times new roman", 30, "bold"), bg= "White", fg= "Black")
        title_lbl.place(x = 0, y = 0, width = screen_width, height = 45)

        # time
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl, font = ('times new roman', 14, 'bold'), background='white', foreground= "black")
        lbl.place(x = 0, y = 0, width= 110, height= 50)
        time()

        # Student button
        imgStudent = Image.open(r"Pictures\student.jpg")
        imgStudent = imgStudent.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimgStudent = ImageTk.PhotoImage(imgStudent)

        b1 = Button(bg_img, image= self.photoimgStudent,command=self.student_details, cursor= "hand2")
        b1.place(x = 200, y = 100, width= 220, height= 220)

        b1_1 = Button(bg_img, text= "Student Details",command=self.student_details, cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 200, y = 300, width= 220, height= 40)

        # Detect Face button
        img4 = Image.open(r"Pictures\face.jpg")
        img4 = img4.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,command = self.f_recongition, image= self.photoimg4, cursor= "hand2")
        b1.place(x = 500, y = 100, width= 220, height= 220)

        b1_1 = Button(bg_img,command = self.f_recongition, text= "Face Detector", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 500, y = 300, width= 220, height= 40)

        # Attendance button
        img5 = Image.open(r"Pictures\attendance.png")
        img5 = img5.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, command = self.attendance, image= self.photoimg5, cursor= "hand2")
        b1.place(x = 800, y = 100, width= 220, height= 220)

        b1_1 = Button(bg_img, command = self.attendance, text= "Attendance", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 800, y = 300, width= 220, height= 40)

        # Help desk button
        img6 = Image.open(r"Pictures\HD.jpeg")
        img6 = img6.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, command = self.helpDesk, image= self.photoimg6, cursor= "hand2")
        b1.place(x = 1100, y = 100, width= 220, height= 220)

        b1_1 = Button(bg_img, command = self.helpDesk, text= "Help Desk", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 1100, y = 300, width= 220, height= 40)

        # Train button
        imgTrain = Image.open(r"Pictures\train.jpg")
        imgTrain = imgTrain.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimgTrain = ImageTk.PhotoImage(imgTrain)

        b1 = Button(bg_img, command = self.train_data_set, image= self.photoimgTrain, cursor= "hand2")
        b1.place(x = 200, y = 380, width= 220, height= 220)

        b1_1 = Button(bg_img, command = self.train_data_set, text= "Train Data", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 200, y = 580, width= 220, height= 40)

        # Photos face button
        img7 = Image.open(r"Pictures\photos.png")
        img7 = img7.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, command = self.photos, image= self.photoimg7, cursor= "hand2")
        b1.place(x = 500, y = 380, width= 220, height= 220)

        b1_1 = Button(bg_img, command = self.photos, text= "Photos", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 500, y = 580, width= 220, height= 40)

        # Developer button
        img8 = Image.open(r"Pictures\developer.jpg")
        img8 = img8.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, command = self.developers, image= self.photoimg8, cursor= "hand2")
        b1.place(x = 800, y = 380, width= 220, height= 220)

        b1_1 = Button(bg_img, command = self.developers, text= "Developer", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 800, y = 580, width= 220, height= 40)

        # Exit button
        img9 = Image.open(r"Pictures\exit.jfif")
        img9 = img9.resize((220, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, command = self.iExit ,image= self.photoimg9, cursor= "hand2")
        b1.place(x = 1100, y = 380, width= 220, height= 220)

        b1_1 = Button(bg_img, command = self.iExit, text= "Exit", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = 1100, y = 580, width= 220, height= 40)


        # Label and Entry fields

    # exit
    def iExit(self):
        try:

            self.exit = tkinter.messagebox.askyesno("Face Recognition", "Do you want to leave?", parent = self.root)
            
            if self.exit > 0:
                self.root.destroy()
            else:
                return

        except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # photos
    def photos(self):
        os.startfile("data")


    # ========================== buttons' functions ==========================
    def student_details(self):
        self.new_window = Toplevel(self.root)   # new window to be opened at the top level
        self.app = Student(self.new_window)

    # train
    def train_data_set(self):
        self.new_window = Toplevel(self.root)   # new window to be opened at the top level
        self.app = Train(self.new_window)
    
    # Face Recongnition
    def f_recongition(self):
        self.new_window = Toplevel(self.root)   # new window to be opened at the top level
        self.app = Face_Recongition(self.new_window)

    # Attendance
    def attendance(self):
        self.new_window = Toplevel(self.root)   # new window to be opened at the top level
        self.app = Attendance(self.new_window)

    # developers
    def developers(self):
        self.new_window = Toplevel(self.root)   # new window to be opened at the top level
        self.app = Developers(self.new_window)

    # helpDesk
    def helpDesk(self):
        self.new_window = Toplevel(self.root)   # new window to be opened at the top level
        self.app = HelpDesk(self.new_window)

if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recognition_System(root)
    root.mainloop()