from tkinter import*
from tkinter import ttk # for stylish
from tkinter import messagebox
from PIL import Image, ImageTk  # for image
import mysql.connector 
from time import strftime
from datetime import datetime
import cv2  # openCV 
import os
import numpy as np
from linked_list import LinkedList 


def clean_fetchone(cursor):
    x = cursor.fetchone()
    if x:
        return x[0]
    else:
        return "N/A"

class Face_Recongition:
    def __init__(self, root):
        
        self.root = root
        
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        
        self.root.geometry("{}x{}".format(screen_width, screen_height))
        root.state('zoomed')
        self.root.title("Face Recongition")
        self.root.wm_iconbitmap("faceIcon.ico")
        
        # title lable
        title_lbl = Label(self.root, text = "Face Recongition", font = ("times new roman", 30, "bold"), bg= "White", fg= "Black")
        title_lbl.place(x = 0, y = 0, width = screen_width, height = 45)

        # inserting the 1nd image
        top_img = Image.open(r"Pictures\face.jpg")
        top_img = top_img.resize((int(screen_width), int(screen_height) - 30), Image.LANCZOS)    # convert high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(top_img)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x = 0, y = 48, width = int(screen_width), height = int(screen_height) - 30)

        # botton Recognition
        thirdOfScreen_width = int(screen_width / 5)

        b1_1 = Button(f_lbl, command = self.face_recog, text= "Face Recongition", cursor = "hand2", font = ("times new roman", 15, "bold"), bg= "lightgreen", fg= "black")
        b1_1.place(x = 235, y = 570, width= thirdOfScreen_width - 37, height= 45)

        img6 = Image.open(r"Pictures\process.jpg")
        img6 = img6.resize((500, 220), Image.LANCZOS)    # convert high level image to low level
        self.photoimg19 = ImageTk.PhotoImage(img6)

    # attendace
    def mark_Attendance(self, i, r, n, d):
        with open(r"Attendance_Report\Attendance.csv", "r+", newline= "\n") as f: # excel file
            myDataList = f.readlines()
            # name_list = []  # list
            name_list = LinkedList()
            for line in myDataList:
                entry = line.split((","))   # Muhammad,391855, department
                name_list.append(entry[0])

            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {d}, {dtString}, {date}, Present")
        
        f.close()

    #  Face Recognition
    def face_recog(self):
        try:
            def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                # coord = [] # list
                coord = LinkedList()

                for (x, y, w, h) in features:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    confidence = int((100*(1-predict/300)))     # Formula
                    
                    # creaate database
                    conn = mysql.connector.connect(host = "localhost", username= "root", password= "rootpassword", database= "face_recogizer")
                    my_cursor = conn.cursor()
                    

                    # name
                    my_cursor.execute("Select studentName from student where studentID =" + str(id))
                    n = clean_fetchone(my_cursor)    # only for the name

                    # Roll number
                    my_cursor.execute("Select rollNumber from student where studentID =" + str(id))
                    r = clean_fetchone(my_cursor)

                    # department
                    my_cursor.execute("Select course from student where studentID =" + str(id))
                    d = clean_fetchone(my_cursor)
            
                    my_cursor.execute("Select studentID from student where studentID =" + str(id))
                    i = clean_fetchone(my_cursor)
                    conn.close()

                    if n == "N/A" or r == "N/A" or d == "N/A":
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    elif confidence > 75:
                        cv2.putText(img, f"ID: " + i, (x, y-75), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"CMS ID: " + r, (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Name: {n}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        cv2.putText(img, f"Course: {d}", (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                        self.mark_Attendance(i, r, n, d)
                    else:
                        # For unknown face
                        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                        cv2.putText(img, "Unknown Face", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)

                    coord.insert_values([x, y, w, h])

                return coord

            def recognize(img, clf, faceCascade):
                coord = draw_boundray(img, faceCascade, 1.1, 10, (255, 255, 255), "Face", clf)
                return img
           
            path = 'dataset'
            faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            clf = cv2.face_LBPHFaceRecognizer.create()
            clf.read("classifer.xml")

            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                img = recognize(img, clf, faceCascade)
                cv2.imshow("Welcome to Face Recognition", img)

                if cv2.waitKey(1) == 13:
                    break

            video_cap.release()
            cv2.destroyAllWindows()
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

if __name__ == "__main__":
    root = Tk() 
    obj = Face_Recongition(root)
    root.mainloop()