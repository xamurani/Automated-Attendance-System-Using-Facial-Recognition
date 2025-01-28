## Automated Attendance System Using Facial Recognition

An efficient and automated attendance tracking system utilizing facial recognition technology. This application detects faces in real-time, matches them against a registered database, and logs attendance accurately. Built with Python and OpenCV, it is ideal for educational institutions and workplaces aiming to streamline attendance management.

# Table of Contents

Features

Prerequisites

Installation

Usage

Project Structure

Contributing

License

Acknowledgements


# Features

Real-Time Face Detection: Captures and identifies faces in real-time using OpenCV.

Database Integration: Matches detected faces with a pre-registered database of individuals.

Automated Attendance Logging: Records attendance automatically upon successful face recognition.

User-Friendly Interface: Simple and intuitive interface for ease of use.

Secure Access: Login system to ensure authorized access to the application.


# Prerequisites

Before running this application, ensure you have the following installed:

Python 3.x: The programming language used for development.

OpenCV: Library for real-time computer vision.

NumPy: Library for numerical computations.

Pandas: Data manipulation and analysis library.

Tkinter: Standard GUI toolkit for Python.


# Installation

1. Clone the Repository:

git clone ''' https://github.com/xamurani/Automated-Attendance-System-Using-Facial-Recognition.git
cd Automated-Attendance-System-Using-Facial-Recognition '''


2. Install Dependencies:

It's recommended to use a virtual environment to manage dependencies.

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt

If requirements.txt is not available, manually install the required libraries:

pip install opencv-python numpy pandas


3. Prepare the Database:

Ensure that the data and database directories exist in the project root. The data directory will store images of registered individuals, and the database directory will contain the SQLite database for attendance records.



# Usage

1. Run the Application:

python main.py


2. Login:

Enter your credentials on the login screen. Default credentials can be set in the login.py file.



3. Register a New Student:

Navigate to the "Student" section.

Enter the student's details and capture their images to register them in the system.



4. Mark Attendance:

Navigate to the "Attendance" section.

The system will automatically detect and recognize faces, marking attendance for recognized individuals.



5. View Attendance Reports:

Navigate to the "Attendance_Report" section to view and export attendance records.




# Project Structure

Automated-Attendance-System-Using-Facial-Recognition/
├── Attendance_Report/
├── Login Page/
├── Pictures/
├── __pycache__/
├── data/
├── database/
├── Attendance.csv
├── DSA Project Proposal.docx
├── Project Idea.docx
├── README.md
├── attendance.py
├── classifer.xml
├── developers.py
├── faceIcon.ico
├── faceIcon.png
├── face_recongnition.py
├── haarcascade_frontalface_default.xml
├── helpDesk.py
├── linked_list.py
├── login.py
├── main.py
├── setup.py
└── student.py

Attendance_Report/: Contains generated attendance reports.

Login Page/: Assets related to the login interface.

Pictures/: Stores captured images for face recognition.

data/: Contains images of registered individuals.

database/: SQLite database storing attendance records.

attendance.py: Handles attendance marking logic.

face_recongnition.py: Core facial recognition functionalities.

haarcascade_frontalface_default.xml: Pre-trained model for face detection.

login.py: Manages user authentication.

main.py: Entry point of the application.

student.py: Manages student registration and data handling.


# Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.


2. Create a new branch (git checkout -b feature-branch).


3. Commit your changes (git commit -m 'Add new feature').


4. Push to the branch (git push origin feature-branch).


5. Open a Pull Request.



# License

This project is licensed under the MIT License. See the LICENSE file for details.

# Acknowledgements

OpenCV: For providing the computer vision library.

NumPy: For numerical computations.

Pandas: For data manipulation and analysis.

Tkinter: For the GUI toolkit.


