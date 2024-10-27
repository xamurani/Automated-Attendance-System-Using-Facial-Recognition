from tkinter import*
from tkinter import ttk # for stylish
from tkinter import messagebox
from PIL import Image, ImageTk  # for image
import mysql.connector 
import cv2 as cv    # openCV
import os
import numpy as np

from linked_list import LinkedList

class Train:
    def __init__(self, root):
        
        self.root = root
        
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        
        self.root.geometry("{}x{}".format(screen_width, screen_height))
        root.state('zoomed')
        self.root.title("Train Data Sample")
        self.root.wm_iconbitmap("faceIcon.ico")


        # title lable
        title_lbl = Label(self.root, text = "Train Data Set", font = ("times new roman", 30, "bold"), bg= "White", fg= "Black")
        title_lbl.place(x = 0, y = 0, width = screen_width, height = 45) 

        # inserting the 1nd image
        top_img = Image.open(r"Pictures\train.jpg")
        top_img = top_img.resize((int(screen_width), int(screen_height) - 30), Image.LANCZOS)    # convert high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x = 0, y = 48, width = int(screen_width), height = int(screen_height) - 30)

        # botton Train
        thirdOfScreen_width = int(screen_width / 5)

        b1_1 = Button(self.root, command = self.train_classifier, text= "Train Data", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "Black")
        b1_1.place(x = thirdOfScreen_width + thirdOfScreen_width - 2, y = 690, width= thirdOfScreen_width - 37, height= 45)

    def train_classifier(self):
        try:
            data_dir = (r"data")
            path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

            # faces = []
            # ids = []

            faces = LinkedList()
            ids = LinkedList()

            for image in path:
                img = Image.open(image).convert('L')    # Gray scale image
                imageNp = np.array(img, 'uint8')
                id = int (os.path.split(image)[1].split('.')[1])

                faces.append(imageNp)
                ids.append(id)
                cv.imshow("Training", imageNp)
                cv.waitKey(1) == 13

            faces_array = faces.linked_list_to_numpy_array()
            ids_array = ids.linked_list_to_numpy_array()

            # ======================= Train the classifier and save ============

            path = 'dataset'
            recognizer = cv.face_LBPHFaceRecognizer.create()

            detector = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


            recognizer.train(faces_array, ids_array)

            recognizer.write("classifer.xml")
            cv.destroyAllWindows()
            messagebox.showinfo("Result","Training dataset completed...!!!", parent = self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

if __name__ == "__main__":
    root = Tk() 
    obj = Train(root)
    root.mainloop()