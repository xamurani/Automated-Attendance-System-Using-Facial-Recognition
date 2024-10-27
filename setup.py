import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Muhammad\AppData\Local\Programs\Python\Python311\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Muhammad\AppData\Local\Programs\Python\Python311\tcl\tk8.6"

executables = [cx_Freeze.Executable("login.py", base=base, icon="faceIcon.ico")]


cx_Freeze.setup(
    name = "Automated Attendance System Using Facial Recognition",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["faceIcon.ico",'tcl86t.dll','tk86t.dll', 'Pictures','data','database','Attendance_Report', 'DSA_project_Ali']}},
    version = "1.0",
    description = "We have designed and programmed Automated Attendance System Using Facial Recognition in our end semester project of DSA | Developed By Muhammad and Muhammad Ali",
    executables = executables
    )
