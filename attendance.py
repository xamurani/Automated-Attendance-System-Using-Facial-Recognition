from tkinter import*
from tkinter import ttk # for stylish
from tkinter import messagebox

from PIL import Image, ImageTk  # for image
import os   # for photos
import csv
from tkinter import filedialog
import easygui

from linked_list import LinkedList

# myData = []     # global varibale
myData = LinkedList()


class Attendance:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1530x798+0+0")
        self.root.geometry("1600x800+0+0")
        root.state('zoomed')
        self.root.title("Automated Attendance System Using Facial Recognition")
        #root.resizable(False, False)
        self.root.wm_iconbitmap("faceIcon.ico")
        
        # variables 
        self.var_attendance_id = StringVar()
        self.var_attendance_roll = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_dep = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance = StringVar()
        
        screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
        # self.root.wm_attributes('-transpatentcolor, ', '#ab23ff')

        # Inserting the 1st image
        img01 = Image.open(r"Pictures\attendance01.png")
        img01 = img01.resize((int(screen_width), 250), Image.LANCZOS)    # convert high level image to low level
        self.photoimg1 = ImageTk.PhotoImage(img01)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x = 0, y = 0, width = int(screen_width), height = 250)
        
        # Main Frame
        mainFrame = ttk.Frame(self.root, relief=RIDGE)
        mainFrame.place(x = 0, y = 250, width = int(screen_width), height =  int(screen_height))
        
        # frame.place(anchor='center', relx=0.5, rely=0.5)
        
        # top label frame (Student Attendance Details)
        # top_frame = LabelFrame(mainFrame, bd = 2, bg="white", relief=RIDGE, text="Student Attendance Details", font = ("times new roman", 12, "bold"))
        top_frame = LabelFrame(mainFrame, text = "Student Attendance Details")
        top_frame.place(x = 10, y = 10, width= int(screen_width) - 25, height= 250)

        # A Frame Inside the Top Frame
        insideTopFrame = ttk.Frame(top_frame, relief=RIDGE)
        insideTopFrame.place(x = 10, y = 0, width = int(screen_width) - 50, height =  220)

        # Attendance ID
        attendanceID_label = ttk.Label(insideTopFrame, text = "Attendance ID:", font = ("times new roman", 12, "bold"))
        attendanceID_label.grid(row=0, column=0, padx = 10, pady= 5, sticky= W)

        attendanceID_entry = ttk.Entry(insideTopFrame, textvariable = self.var_attendance_id, font = ("times new roman", 12))
        attendanceID_entry.grid(row= 0, column=1, pady= 5, sticky=W)
        
        # Name
        name_label = ttk.Label(insideTopFrame, text = "Name:", font = ("times new roman", 12, "bold"))
        name_label.grid(row=0, column=2, padx = 10, pady= 5, sticky= W)

        name_entry = ttk.Entry(insideTopFrame, textvariable = self.var_attendance_name, font = ("times new roman", 12))
        name_entry.grid(row= 0, column=3, pady= 5, sticky=W)

        # Department
        department_label = ttk.Label(insideTopFrame, text = "Course:", font = ("times new roman", 12, "bold"))
        department_label.grid(row=0, column=4, padx = 10, pady= 5, sticky= W)

        department_entry = ttk.Entry(insideTopFrame, textvariable = self.var_attendance_dep, font = ("times new roman", 12))
        department_entry.grid(row= 0, column=5, pady= 5, sticky=W)

        # Time
        time_label = ttk.Label(insideTopFrame, text = "Time:", font = ("times new roman", 12, "bold"))
        time_label.grid(row=0, column=6, padx = 10, pady= 5, sticky= W)

        time_entry = ttk.Entry(insideTopFrame, textvariable = self.var_attendance_time, font = ("times new roman", 12))
        time_entry.grid(row= 0, column=7, pady= 5, sticky=W)

        # Date
        date_label = ttk.Label(insideTopFrame, text = "Date:", font = ("times new roman", 12, "bold"))
        date_label.grid(row=0, column=8, padx = 10, pady= 5, sticky= W)

        date_entry = ttk.Entry(insideTopFrame, textvariable = self.var_attendance_date, font = ("times new roman", 12))
        date_entry.grid(row= 0, column=9, pady= 5, sticky=W)

        # Attendance Status
        attendanceStatus_label = ttk.Label(insideTopFrame, text = "Attendance Status:", font = ("times new roman", 12, "bold"))
        attendanceStatus_label.grid(row=0, column=10, padx = 10, pady= 5, sticky= W)

        self.attendance_status = ttk.Combobox(insideTopFrame,textvariable = self.var_attendance, width= 13, font= "comicsansns 11", state= "readonly")
        self.attendance_status["values"] = ("Status", "Present", "Absent", "Leave")
        self.attendance_status.grid(row = 0, column=11, pady = 8)
        self.attendance_status.current(0)

        # Button Frame
        buttonFrame = ttk.Frame(insideTopFrame, relief=RIDGE)
        buttonFrame.place(x = 820, y = 140 + (70 - 35), width= 720, height= 35)

        # Import CSV button
        save_buttonn = Button(buttonFrame, command = self.importCSV, text= "Import CSV", width=17, font = ("times new roman", 13, "bold"), bg="Green", fg="White")
        save_buttonn.grid(row=0, column= 0)

        # Export CSV button
        save_buttonn = Button(buttonFrame, command = self.exportCSV, text= "Export CSV", width=17, font = ("times new roman", 13, "bold"), bg="Yellow", fg="Black")
        save_buttonn.grid(row=0, column= 1)

        # Update button
        save_buttonn = Button(buttonFrame,command = self.update, text= "Update", width=17, font = ("times new roman", 13, "bold"), bg="Red", fg="White")
        save_buttonn.grid(row=0, column= 2)

        # Reset button
        save_buttonn = Button(buttonFrame, command = self.reset, text= "Reset", width=17, font = ("times new roman", 13, "bold"), bg = "gray")
        save_buttonn.grid(row=0, column= 3)


        # Lower label frame (Attendance Details)
        lower_frame = LabelFrame(mainFrame, text = "Attendance Details")
        lower_frame.place(x = 10, y = 270, width= int(screen_width) - 25, height= 250)

        # Tabble Frame
        tableFrame = ttk.Frame(lower_frame, relief=RIDGE)
        tableFrame.place(x = 10, y = 0, width = int(screen_width) - 50, height =  220)

        # ===================== Scroll Bar Table ================================
        scroll_x = ttk.Scrollbar(tableFrame, orient= HORIZONTAL)
        scroll_y = ttk.Scrollbar(tableFrame, orient= VERTICAL)


        self.atttendanceReportTable = ttk.Treeview(tableFrame, columns= ("ID", "CMS", "Name", "Course", "Time", "Date", "Attendance"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.atttendanceReportTable.xview)
        scroll_y.config(command = self.atttendanceReportTable.yview)

        self.atttendanceReportTable.heading("ID", text = "Attendance ID")
        self.atttendanceReportTable.heading("CMS", text = "CMS ID")
        self.atttendanceReportTable.heading("Name", text = "Name")
        self.atttendanceReportTable.heading("Course", text = "Course")
        self.atttendanceReportTable.heading("Time", text = "Time")
        self.atttendanceReportTable.heading("Date", text = "Date")
        self.atttendanceReportTable.heading("Attendance", text = "Attendance")
        
        self.atttendanceReportTable["show"] = "headings"

        self.atttendanceReportTable.column("ID", width = 100)
        self.atttendanceReportTable.column("CMS", width = 100)
        self.atttendanceReportTable.column("Name", width = 100)
        self.atttendanceReportTable.column("Course", width= 100)
        self.atttendanceReportTable.column("Time", width = 100)
        self.atttendanceReportTable.column("Date", width = 100)
        self.atttendanceReportTable.column("Attendance", width = 100)

        self.atttendanceReportTable.pack(fill = BOTH, expand = 1)      
        self.atttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)  

    # =================== fetch Data ===============

    def fetchData(self, rows):
        try:
            
            self.atttendanceReportTable.delete(*self.atttendanceReportTable.get_children())    # deleting the existing data in the attendanceReportTable
            # inserting the data 
            
            for i in rows:
                self.atttendanceReportTable.insert("", END, values = i)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # import CSV File
    def importCSV(self):
        try:

            global myData
            myData.clear()
            fileName = filedialog.askopenfilename(initialdir = os.getcwd(), title="Open CSV File", filetypes= (("csv File", "*.csv"), ("All File", "*.*")), parent = self.root)
            with open(fileName) as myFile:
                
                csvread = csv.reader(myFile, delimiter = ",")
                
                for i in csvread:
                    myData.append(i)

                self.fetchData(myData)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # update
    def update(self):
        try:
        # Open the CSV file in read mode and create a reader object
            with open('Attendance_Report//Attendance.csv', 'r') as file:
                reader = csv.reader(file)

                # Create a list of rows
                rows = list(reader)

            # Find the row you want to edit.
            myvar = easygui.enterbox("Enter the row index to update the attendance of a student.")
            row_to_edit = int(myvar)

            # Modify the desired cell value in the row
            rows[row_to_edit][0] = self.var_attendance_id.get()
            rows[row_to_edit][1] = self.var_attendance_roll.get()
            rows[row_to_edit][2] = self.var_attendance_name.get()
            rows[row_to_edit][3] = self.var_attendance_dep.get()
            rows[row_to_edit][4] = self.var_attendance_time.get()
            rows[row_to_edit][5] = self.var_attendance_date.get()
            rows[row_to_edit][6] = self.var_attendance.get()


            # Open the CSV file in write mode and create a writer object
            with open('Attendance.csv', 'w', newline='') as file:
                writer = csv.writer(file)

                # Write the modified rows to the CSV file
                writer.writerows(rows)
                messagebox.showinfo("Attendance Update", "Attendance updated successfully.", parent = self.root)
                self.fetchData(rows)
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)

    # Export CSV File
    def exportCSV(self):
        try:
            # if len(myData) < 1:
            if myData.get_length < 1:
                messagebox.showerror("No Data", "No any data found to export.", parent = self.root)
                return False

            fileName = filedialog.asksaveasfilename(initialdir = os.getcwd(), title="Open CSV File", filetypes= (("csv File", "*.csv"), ("All File", "*.*")), parent = self.root)    
            with open(fileName, mode = "w", newline= "") as myFile:
                exportWrite = csv.writer(myFile, delimiter= ",")

                for i in myData:
                    exportWrite.writerow(i)
                
                messagebox.showinfo("Data Export", "Your data exported to " + os.path.basename(fileName) + " file successfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)  

    # get_cursor
    def get_cursor(self, event = ""):
        try:
            cursor_row = self.atttendanceReportTable.focus()
            content = self.atttendanceReportTable.item(cursor_row)
            rows = content['values']
            
            self.var_attendance_id.set(rows[0])
            self.var_attendance_roll.set(rows[1])
            self.var_attendance_name.set(rows[2])
            self.var_attendance_dep.set(rows[3])
            self.var_attendance_time.set(rows[4])
            self.var_attendance_date.set(rows[5])
            self.var_attendance.set(rows[6])
        except Exception as es:
            messagebox.showerror("Error", f"Due To :{str(es)}", parent = self.root)    

    # reset
    def reset(self):

            self.var_attendance_id.set("")
            self.var_attendance_roll.set("")
            self.var_attendance_name.set("")
            self.var_attendance_dep.set("")
            self.var_attendance_time.set("")
            self.var_attendance_date.set("")
            self.var_attendance.set("")
            
if __name__ == "__main__":
    root = Tk() 
    obj = Attendance(root)
    root.mainloop()