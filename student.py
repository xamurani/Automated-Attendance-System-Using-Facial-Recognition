from tkinter import*
from tkinter import ttk # for stylish
from tkinter import messagebox
from PIL import Image, ImageTk  # for image
import mysql.connector 
import cv2      # openCV 

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x798+0+0")
        #self.root.geometry("1600x800+0+0")
        root.state('zoomed')
        self.root.title("Student Details")
        self.root.wm_iconbitmap("faceIcon.ico")
        
        # variables
        self.var_dep = StringVar()
        self.var_cur = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_stdID = StringVar()
        self.var_stdName = StringVar()
        self.var_clsDiv = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_birthDate = StringVar()
        self.var_emailAddress = StringVar()
        self.var_phoneNo = StringVar()
        self.var_teacherName = StringVar()
        self.var_Address = StringVar()

        self.var_search = StringVar()

        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()

        # inserting the 1st image
        img = Image.open(r"Pictures\third.jpg")
        img = img.resize((int(screen_width / 3), 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x = 0, y = 0, width = int(screen_width / 3), height = 130)

        # inserting the 2nd image
        img1 = Image.open(r"Pictures\second.jpg")
        img1 = img1.resize((int(screen_width / 3), 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x = 500, y = 0, width = int(screen_width / 3), height = 130)

        # inserting the 3rd image
        img2 = Image.open(r"Pictures\first.jpg")
        img2 = img2.resize((int(screen_width / 2.5), 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x = 1000, y = 0, width = int(screen_width / 2.5), height = 130)

        # bg image
        img3 = Image.open(r"Pictures\background1.png")
        img3 = img3.resize((int(screen_width), int(screen_height)), Image.LANCZOS)    # convert high level image to low level
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x = 0, y = 130, width = int(screen_width), height = int(screen_height))

        # title lable
        title_lbl = Label(bg_img, text = "STUDENT MANAGEMENT SYSTEM", font = ("times new roman", 30, "bold"), bg= "White", fg= "Black")
        title_lbl.place(x = 0, y = 0, width = int(screen_width), height = 45)

        # Frame
        main_frame = Frame(bg_img, bd= 2, bg= "white")
        main_frame.place(x = 60, y = 70, width = 1480, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd = 2, bg="white", relief=RIDGE, text="Student Details", font = ("times new roman", 12, "bold"))
        Left_frame.place(x = 10, y = 10, width= 760, height= 580)

        # Inserting image in the left label
        img_left = Image.open(r"Pictures\second.jpg")
        img_left = img_left.resize((745, 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x = 5, y = 0, width = 745, height = 130)

        # Current Course Information
        current_course_frame = LabelFrame(Left_frame, bd = 2, bg="white", relief=RIDGE, text="Current Course Information", font = ("times new roman", 12, "bold"))
        current_course_frame.place(x = 5, y = 135, width= 745, height= 115)

        # Department
        dep_label = Label(current_course_frame, text = "Department", font = ("times new roman", 12, "bold"), bg = "white")
        dep_label.grid(row=0, column=0, padx = 10)

        dep_combo= ttk.Combobox(current_course_frame, textvariable= self.var_dep, font = ("times new roman", 12, "bold"), width=17, state = "read only")
        dep_combo["values"] = ("Select Department", "Computer Science")
        dep_combo.current(0)
        dep_combo.grid(row=0, column=1, padx = 2, pady = 10)

        # Course
        course_label = Label(current_course_frame, text = "Course", font = ("times new roman", 12, "bold"), bg = "white")
        course_label.grid(row=0, column=2, padx = 10, pady= 10)

        course_combo= ttk.Combobox(current_course_frame, textvariable=self.var_cur, font = ("times new roman", 12, "bold"), width=17, state = "read only")
        course_combo["values"] = ("Select Course", "Data Structures and Algorithms", "Database Systems", "Computer Organization and Assembly Languages", "Linear Algebra", "Techinal Writing")
        course_combo.current(0)
        course_combo.grid(row=0, column=3, padx = 2, pady = 10, sticky= W)

        # Year
        year_label = Label(current_course_frame, text = "Year", font = ("times new roman", 12, "bold"), bg = "white")
        year_label.grid(row=1, column=0, padx = 10, sticky= W)

        year_combo= ttk.Combobox(current_course_frame,textvariable=self.var_year ,font = ("times new roman", 12, "bold"), width=17, state = "read only")
        year_combo["values"] = ("Select Year", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26")
        year_combo.current(0)
        year_combo.grid(row=1, column=1, padx = 2, pady = 10, sticky= W)

        # Semester
        semester_label = Label(current_course_frame, text = "Semester", font = ("times new roman", 12, "bold"), bg = "white")
        semester_label.grid(row=1, column=2, padx = 10, sticky= W)

        semester_combo= ttk.Combobox(current_course_frame, textvariable=self.var_sem, font = ("times new roman", 12, "bold"), width=17, state = "read only")
        semester_combo["values"] = ("Select Semester", "Semester-I", "Semester-II", "Semester-III", "Semester-IV", "Semester-V", "Semester-VI", "Semester-VII")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 3, padx = 2, pady = 10, sticky = W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame, bd = 2, bg="white", relief=RIDGE, text="Class Student Information", font = ("times new roman", 12, "bold"))
        class_student_frame.place(x = 5, y = 250, width= 745, height= 300)

        # StudentID
        studentID_label = Label(class_student_frame, text = "StudentID:", font = ("times new roman", 12, "bold"), bg = "white")
        studentID_label.grid(row=0, column=0, padx = 10, pady= 5, sticky= W)

        StudentID_entry = ttk.Entry(class_student_frame, textvariable=self.var_stdID, font = ("times new roman", 12))
        StudentID_entry.grid(row= 0, column=1, padx= 10, pady= 5, sticky=W)

        # Student Name
        student_name_label = Label(class_student_frame, text = "Student Name:", font = ("times new roman", 12, "bold"), bg = "white")
        student_name_label.grid(row=0, column=3, padx = 10, pady= 5, sticky= W)

        StudentName_entry = ttk.Entry(class_student_frame, textvariable=self.var_stdName, font = ("times new roman", 12))
        StudentName_entry.grid(row= 0, column=4, padx= 10, pady= 5, sticky=W)

        # Class didvision
        class_div_label = Label(class_student_frame, text = "Class Division:", font = ("times new roman", 12, "bold"), bg = "white")
        class_div_label.grid(row=1, column=0, padx = 10, pady= 5, sticky= W)

        class_div_entry = ttk.Entry(class_student_frame, textvariable=self.var_clsDiv, font = ("times new roman", 12))
        class_div_entry.grid(row= 1, column=1, padx= 10, pady= 5, sticky=W)

        # Roll Number
        roll_num_label = Label(class_student_frame, text = "Roll Number:", font = ("times new roman", 12, "bold"), bg = "white")
        roll_num_label.grid(row=1, column=3, padx = 10, pady= 5, sticky= W)

        roll_num_entry = ttk.Entry(class_student_frame, textvariable=self.var_roll, font = ("times new roman", 12))
        roll_num_entry.grid(row= 1, column=4, padx= 10, pady= 5, sticky=W)

        # Gender
        gender_label = Label(class_student_frame, text = "Gender:", font = ("times new roman", 12, "bold"), bg = "white")
        gender_label.grid(row=2, column=0, padx = 10, pady= 5, sticky= W)

        gender_entry = ttk.Entry(class_student_frame, textvariable=self.var_gender, font = ("times new roman", 12))
        gender_entry.grid(row=2, column=1, padx= 10, pady= 5, sticky=W)

        # Birth Date
        birth_date_label = Label(class_student_frame, text = "Birth Date:", font = ("times new roman", 12, "bold"), bg = "white")
        birth_date_label.grid(row=2, column=3, padx = 10, pady= 5, sticky= W)

        birth_date_entry = ttk.Entry(class_student_frame, textvariable=self.var_birthDate, font = ("times new roman", 12))
        birth_date_entry.grid(row=2, column=4, padx= 10, pady= 5, sticky=W)

        # Email
        email_label = Label(class_student_frame, text = "Email Address:", font = ("times new roman", 12, "bold"), bg = "white")
        email_label.grid(row=3, column=0, padx = 10, pady= 5, sticky= W)

        email_entry = ttk.Entry(class_student_frame, textvariable=self.var_emailAddress, font = ("times new roman", 12))
        email_entry.grid(row=3, column=1, padx= 10, pady= 5, sticky=W)

        # Phone Number
        phone_no_label = Label(class_student_frame, text = "Phone No:", font = ("times new roman", 12, "bold"), bg = "white")
        phone_no_label.grid(row=3, column=3, padx = 10, pady= 5, sticky= W)

        phone_no_entry = ttk.Entry(class_student_frame, textvariable=self.var_phoneNo,font = ("times new roman", 12))
        phone_no_entry.grid(row=3, column=4, padx= 10, pady= 5, sticky=W)

        # Teacher Name
        teacher_name_label = Label(class_student_frame, text = "Teacher Name:", font = ("times new roman", 12, "bold"), bg = "white")
        teacher_name_label.grid(row=4, column=0, padx = 10, pady= 5, sticky= W)

        teacher_name_entry = ttk.Entry(class_student_frame, textvariable=self.var_teacherName, font = ("times new roman", 12))
        teacher_name_entry.grid(row=4, column=1, padx= 10, pady= 5, sticky=W)

        # Address
        address_label = Label(class_student_frame, text = "Address:", font = ("times new roman", 12, "bold"), bg = "white")
        address_label.grid(row=4, column=3, padx = 10, pady= 5, sticky= W)

        address_entry = ttk.Entry(class_student_frame, textvariable=self.var_Address, font = ("times new roman", 12))
        address_entry.grid(row=4, column=4, padx= 10, pady= 5, sticky=W)

        # Radio button 01
        self.var_radtio01 = StringVar()     #variable
        radiobutton01 = ttk.Radiobutton(class_student_frame, variable= self.var_radtio01, text= "Take Photo Simple", value= "Yes")
        radiobutton01.grid(row=6, column=0, padx = 10)

        # Radio button 02
        radiobutton02 = ttk.Radiobutton(class_student_frame, variable= self.var_radtio01, text= "No Photo Simple", value= "NO")
        radiobutton02.grid(row=6, column=1, padx = 10)

        # Button Frame
        buttonFrame = Frame(class_student_frame, bd= 2, bg="white", relief=RIDGE)
        buttonFrame.place(x = 10, y = 200, width= 723, height= 70)

        # Save button
        save_buttonn = Button(buttonFrame, command= self.add_data, text= "Save", width=17, font = ("times new roman", 13, "bold"), bg="Green", fg="White")
        save_buttonn.grid(row=0, column= 0)

        # update button
        save_buttonn = Button(buttonFrame, command = self.update_data, text= "Update", width=17, font = ("times new roman", 13, "bold"), bg="Yellow", fg="Black")
        save_buttonn.grid(row=0, column= 1)

        # Delete button
        save_buttonn = Button(buttonFrame, command= self.delete_data, text= "Delete", width=17, font = ("times new roman", 13, "bold"), bg="Red", fg="White")
        save_buttonn.grid(row=0, column= 2)

        # Reset button
        save_buttonn = Button(buttonFrame, command= self.reset_data, text= "Reset", width=17, font = ("times new roman", 13, "bold"), bg = "gray")
        save_buttonn.grid(row=0, column= 3)

        buttonFrame01 = Frame(class_student_frame, bd= 2, bg="white", relief=RIDGE)
        buttonFrame01.place(x = 10, y = 235, width= 723, height= 35)

        # Take Photo Sample button
        take_photo_buttonn = Button(buttonFrame01, command = self.generateDataSet, text= "Take Photo Sample", width=35, font = ("times new roman", 13, "bold"), bg="skyblue", fg="black")
        take_photo_buttonn.grid(row=0, column= 0)

        # Update Photo button
        update_photo_buttonn = Button(buttonFrame01, command = self.generateDataSet, text= "Update Photo Sample", width=35, font = ("times new roman", 13, "bold"), bg= "yellow", fg = "black")
        update_photo_buttonn.grid(row=0, column= 1)

        # Right label frame
        Right_frame = LabelFrame(main_frame, bd = 2, bg="white", relief=RIDGE, text="Student Details", font = ("times new roman", 12, "bold"))
        Right_frame.place(x = 780, y = 10, width= 685, height= 580)

        # Inserting image in the Right label
        img_right = Image.open(r"C:\Users\Muhammad\OneDrive - National University of Sciences & Technology\Desktop\DSAProject\Pictures\second.jpg")
        img_right = img_left.resize((745, 130), Image.LANCZOS)    # convert high level image to low level
        self.photoimg_right = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Right_frame, image=self.photoimg_left)
        f_lbl.place(x = 5, y = 0, width = 745, height = 130)

        # ============================== Searching System =======================
        search_frame = LabelFrame(Right_frame, bd = 2, bg="white", relief=RIDGE, text="Current Course Information", font = ("times new roman", 12, "bold"))
        search_frame.place(x = 5, y = 135, width= 670, height= 70)

        # Search Label
        Search_label = Label(search_frame, text = "Search By:", font = ("times new roman", 12, "bold"), bg = "Red", fg = "white")
        Search_label.grid(row=0, column=0, padx = 10, pady= 5, sticky= W)

        # Search Combox
        search_combo= ttk.Combobox(search_frame, font = ("times new roman", 12, "bold"), width=17, state = "read only")
        search_combo["values"] = ("Student ID", "")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx = 2, pady = 10, sticky= W)

        # Search Entry
        search_entry = ttk.Entry(search_frame, textvariable = self.var_search, font = ("times new roman", 12))
        search_entry.grid(row=0, column=2, padx= 4)

        # Search button
        search_buttonn = Button(search_frame, command = self.search, text= "Search", width=9, font = ("times new roman", 13, "bold"), bg="Green", fg="White")
        search_buttonn.grid(row=0, column= 3, padx= 5)

        # Show All button
        show_all_buttonn = Button(search_frame, command = self.fatch_data,text= "Show All", width=9, font = ("times new roman", 13, "bold"), bg="Yellow", fg="Black")
        show_all_buttonn.grid(row=0, column= 4, padx= 5)

        # ========================= table Frame =====================================
        table_frame = Frame(Right_frame, bd = 2, bg="white", relief=RIDGE)
        table_frame.place(x = 5, y = 210, width= 670, height= 300)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame, columns=("department", "course", "year", "semester", "studentID", "studentName", "classDivision", "rollNumber", "Gender", "birthDate", "emailAddress", "phoneNo", "teacherName", "address", "photo"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)
  
        scroll_x.pack(side = BOTTOM, fill= X)
        scroll_y.pack(side = RIGHT, fill= Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("department", text= "Department")
        self.student_table.heading("course", text= "Course")
        self.student_table.heading("year", text= "Year")
        self.student_table.heading("semester", text= "Semester")
        self.student_table.heading("studentID", text= "Student ID")
        self.student_table.heading("studentName", text= "Student Name")
        self.student_table.heading("classDivision", text= "Class Division")
        self.student_table.heading("rollNumber", text= "Roll Number")
        self.student_table.heading("Gender", text= "Gender")
        self.student_table.heading("birthDate", text= "Birth Date")
        self.student_table.heading("emailAddress", text= "Email Address")
        self.student_table.heading("phoneNo", text= "Phone Number")
        self.student_table.heading("teacherName", text= "Teacher Name")
        self.student_table.heading("address", text= "Address")
        self.student_table.heading("photo", text= "Photo")
        self.student_table["show"] = "headings"

        self.student_table.column("department", width= 100)
        self.student_table.column("course", width= 100)
        self.student_table.column("year", width= 100)
        self.student_table.column("semester", width= 100)
        self.student_table.column("studentID", width= 100)
        self.student_table.column("studentName", width= 100)
        self.student_table.column("classDivision", width= 100)
        self.student_table.column("rollNumber", width= 100)
        self.student_table.column("Gender", width= 100)
        self.student_table.column("birthDate", width= 100)
        self.student_table.column("emailAddress", width= 100)
        self.student_table.column("phoneNo", width= 100)
        self.student_table.column("teacherName", width= 100)
        self.student_table.column("address", width= 100)
        self.student_table.column("photo", width= 100)

        self.student_table.pack(fill = BOTH, expand= 1)

        self.fatch_data()

        self.student_table.bind("<ButtonRelease>", self.get_cursor)
    
    # ============== functions declaration ==============================
    
    # search
    def search(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="rootpassword", database="face_recogizer")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM student WHERE studentID IN (%s)", (self.var_search.get(),))
            records = my_cursor.fetchall()  # fetch the results of the query
            if records:  # check if there are any records returned
                self.student_table.delete(*self.student_table.get_children())       # delte all the childrens
            
            #inserting by for loop
                for i in records:
                    self.student_table.insert("", END, values = i)
                    conn.commit()
                # print(records)
                # self.fatch_data(records)  # pass the fetched records to the fatch_data method for further processing
            else:
                messagebox.showinfo("No records found", "No records were found for the specified roll number.", parent=self.root)
            conn.close()
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent=self.root)

    # save 
    def add_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdName.get() == "":
            messagebox.showerror("Error", "All Fields are required to be filled.", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host = "localHost", username= "root", password= "rootpassword", database= "face_recogizer")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                                                                                                                        self.var_dep.get(),
                                                                                                                        self.var_cur.get(),
                                                                                                                        self.var_year.get(),
                                                                                                                        self.var_sem.get(),
                                                                                                                        self.var_stdID.get(), 
                                                                                                                        self.var_stdName.get(),
                                                                                                                        self.var_clsDiv.get(),
                                                                                                                        self.var_roll.get(),
                                                                                                                        self.var_gender.get(),
                                                                                                                        self.var_birthDate.get(),
                                                                                                                        self.var_emailAddress.get(),
                                                                                                                        self.var_phoneNo.get(),
                                                                                                                        self.var_teacherName.get(),
                                                                                                                        self.var_Address.get(),
                                                                                                                        self.var_radtio01.get()
                ))
                conn.commit()
                self.fatch_data()
                conn.close()
                messagebox.showinfo("Success", "A student has been added successfully.", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # ==================== fatch data to the table =========================
    def fatch_data(self):
        conn = mysql.connector.connect(host = "localHost", username= "root", password= "rootpassword", database= "face_recogizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:  # means something has been fatched
            self.student_table.delete(*self.student_table.get_children())       # delte all the childrens
            
            #inserting by for loop
            for i in data:
                self.student_table.insert("", END, values = i)
                conn.commit()
        
        conn.close

    # ======================== get cursor ========================
    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0]),
        self.var_cur.set(data[1]),
        self.var_year.set(data[2]),
        self.var_sem.set(data[3]),
        self.var_stdID.set(data[4]), 
        self.var_stdName.set(data[5]),
        self.var_clsDiv.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_birthDate.set(data[9]),
        self.var_emailAddress.set(data[10]),
        self.var_phoneNo.set(data[11]),
        self.var_teacherName.set(data[12]),
        self.var_Address.set(data[13]),
        self.var_radtio01.set(data[14])

    # update
    def update_data(self):
        if self.var_dep.get() == "Select Department" or self.var_stdID.get() == "" or self.var_stdName.get() == "":
            messagebox.showerror("Error", "All Fields are required to be filled.", parent = self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this student's details?", parent = self.root)
                if update > 0:
                    conn = mysql.connector.connect(host = "localHost", username= "root", password= "rootpassword", database= "face_recogizer")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set department = %s, course = %s, year = %s, semester = %s, studentName = %s, classDivision = %s, rollNumber = %s, gender = %s, birthDate = %s, emailAddress = %s, phoneNumber = %s, teacherName = %s, address = %s, photosample = %s where studentID = %s", (
                                                                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                                                                            self.var_cur.get(),
                                                                                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                                                                                            self.var_sem.get(), 
                                                                                                                                                                                                                                                                                            self.var_stdName.get(),
                                                                                                                                                                                                                                                                                            self.var_clsDiv.get(),
                                                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                                                                            self.var_birthDate.get(),
                                                                                                                                                                                                                                                                                            self.var_emailAddress.get(),
                                                                                                                                                                                                                                                                                            self.var_phoneNo.get(),
                                                                                                                                                                                                                                                                                            self.var_teacherName.get(),
                                                                                                                                                                                                                                                                                            self.var_Address.get(),
                                                                                                                                                                                                                                                                                            self.var_radtio01.get(),
                                                                                                                                                                                                                                                                                            self.var_stdID.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success", "A student's details has been successfully updated.", parent = self.root)
                conn.commit()
                self.fatch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # delete 
    def delete_data(self):
        if self.var_stdID.get() == "":
            messagebox.showerror("Error", "Student ID is required to delele a student.", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you want to delele a record?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect(host = "localHost", username= "root", password= "rootpassword", database= "face_recogizer")
                    my_cursor = conn.cursor()
                    sql = "delete from student where studentID = %s"
                    val = (self.var_stdID.get(),)
                    my_cursor.execute(sql, val)
                else:
                    return
                messagebox.showinfo("Success", "A student's details has been successfully deleted.", parent = self.root)
                conn.commit()
                self.fatch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # reset
    def reset_data(self):
        
        self.var_dep.set("Select Department")
        self.var_cur.set("Select Course")
        self.var_year.set("Select Year")
        self.var_sem.set("Select Semester")
        self.var_stdID.set("")
        self.var_stdName.set("")
        self.var_clsDiv.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_birthDate.set("")
        self.var_emailAddress.set("")
        self.var_phoneNo.set("")
        self.var_teacherName.set("")
        self.var_Address.set("")
        self.var_radtio01.set("")

    # ============= Generate Data set or take photo samples ====================
    # Whatever photos we take we need to match them with the photos in the database. ---- 1
    # the photo cannot be inserted or added, due to studentID error, we need to update it.
    def generateDataSet(self):
        try:
            if self.var_dep.get() == "Select Department" or self.var_stdID.get() == "" or self.var_stdName.get() == "":
                messagebox.showerror("Error", "All Fields are required to be filled.", parent = self.root)
            else:
            
                conn = mysql.connector.connect(host = "localHost", username= "root", password= "rootpassword", database= "face_recogizer")
                my_cursor = conn.cursor()
                my_cursor.execute("Select * from student") # selected all data from the database and stored them in the my_result variable below.
                my_result = my_cursor.fetchall() # from the above line we take all the data and stored them inside the result variable.
                
                id = self.var_stdID.get()   # id sy match karna ta images ko jo mara database ka data ha

                # for x in my_result:
                #     id = id + 1

                my_cursor.execute("update student set department = %s, course = %s, year = %s, semester = %s, studentName = %s, classDivision = %s, rollNumber = %s, gender = %s, birthDate = %s, emailAddress = %s, phoneNumber = %s, teacherName = %s, address = %s, photosample = %s where studentID = %s", (
                                                                                                                                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                                                                                                                                            self.var_cur.get(),
                                                                                                                                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                                                                                                                                            self.var_sem.get(), 
                                                                                                                                                                                                                                                                                            self.var_stdName.get(),
                                                                                                                                                                                                                                                                                            self.var_clsDiv.get(),
                                                                                                                                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                                                                            self.var_birthDate.get(),
                                                                                                                                                                                                                                                                                            self.var_emailAddress.get(),
                                                                                                                                                                                                                                                                                            self.var_phoneNo.get(),
                                                                                                                                                                                                                                                                                            self.var_teacherName.get(),
                                                                                                                                                                                                                                                                                            self.var_Address.get(),
                                                                                                                                                                                                                                                                                            self.var_radtio01.get(),
                                                                                                                                                                                                                                                                                            self.var_stdID.get()
                ))

                conn.commit()
                self.fatch_data()
                self.reset_data()
                conn.close()

                # ======= Load predefined data on face frontals from OpenVC Library =======
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") # file loaded inside the 'face_classifier' variable, this file is for object detection.

                def face_cropped(img):
                    try:
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Green, blue and Red images are to be converted into gray scale
                        faces = face_classifier.detectMultiScale(gray, 1.3, 5)  # scaling factor = 1.3, Minimum neighbor = 5


                        for (x, y, w, h) in faces:  # for rectangle
                            face_cropped = img[y: y + h, x: x + w] # img is going to be cropped on the following values
                            return face_cropped
                    except Exception as es:
                        messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)


                # open camera
                cap = cv2.VideoCapture(0)   # 0 for opening the web camera of the laptop, 1 for others and a path for opening a picture can also be passed
                img_id = 0 # becase we need 100 samples
                while True:
                    try:
                        ret, my_frame = cap.read() # firstly images are going to be read.
                        if face_cropped(my_frame) is not None: # means keeps so data
                            img_id = img_id + 1     # incremening
                            face = cv2.resize(face_cropped(my_frame), (450, 450))   # resizing and cropping (passport size)
                            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)   # converting the resized and cropped image into gray scale
                            # storing it
                            file_name_path = "data/user." + str(id) + "." + str(img_id) + ".jpg" # generated picture name with followings id, img_id and .jpg extension.
                            # writing 
                            # saves the imagee
                            cv2.imwrite(file_name_path, face)                             
                            cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2) # oiregn width, color, thickness 
                            cv2.imshow("Cropped Face", face)

                        if cv2.waitKey(1) == 13 or int(img_id) == 100:
                            break
                    except Exception as es:
                        messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)
                
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generating data sets completed!!!", parent = self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)


if __name__ == "__main__":
    root = Tk() 
    obj = Student(root)
    root.mainloop()