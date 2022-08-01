#Student Databaase System Done By Po3
import tkinter as tk
from tkinter import ttk
#from tkinter import ttk, messagebox
import sqlite3

root = tk.Tk()
root.title("Student Database Project by Po3")

connection = sqlite3.connect('sdp.db')

TABLE_NAME = "sdp_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_school = "student_school"
STUDENT_ADDRESS = "student_address"
STUDENT_ROLLNO = "student_rollno"

connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
                   " INTEGER PRIMARY KEY AUTOINCREMENT, " +
                   STUDENT_NAME + " TEXT, " + STUDENT_school + " TEXT, " +
                   STUDENT_ADDRESS + " TEXT, " + STUDENT_ROLLNO + " INTEGER);")

appLabel = tk.Label(root, text="Student Database System", fg="#06a099", width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30, 0))

class Student:
    studentName = ""
    schoolName = ""
    rollnoNumber = 0
    address = ""

    def __init__(self, studentName, schoolName, rollnoNumber, address):
        self.studentName = studentName
        self.schoolName = schoolName
        self.rollnoNumber = rollnoNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                     font=("Times New Roman", 12)).grid(row=1, column=0, padx=(10,0),
                                                pady=(30, 0))
schoolLabel = tk.Label(root, text="Enter your school name", width=40, anchor='w',
                        font=("Times New Roman", 12)).grid(row=2, column=0, padx=(10,0))
rollnoLabel = tk.Label(root, text="Enter your roll number", width=40, anchor='w',
                      font=("Times New Roman", 12)).grid(row=3, column=0, padx=(10,0))
addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                        font=("Times New Roman", 12)).grid(row=4, column=0, padx=(10,0))

nameEntry = tk.Entry(root, width = 30)
schoolEntry = tk.Entry(root, width = 30)
rollnoEntry = tk.Entry(root, width = 30)
addressEntry = tk.Entry(root, width = 30)

nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30, 20))
schoolEntry.grid(row=2, column=1, padx=(0,10), pady = 20)
rollnoEntry.grid(row=3, column=1, padx=(0,10), pady = 20)
addressEntry.grid(row=4, column=1, padx=(0,10), pady = 20)

def takeNameInput():
    global nameEntry, schoolEntry, rollnoEntry, addressEntry
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_school , STUDENT_ADDRESS, STUDENT_ROLLNO
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    schoolName = schoolEntry.get()
    schoolEntry.delete(0, tk.END)
    rollno = (int(rollnoEntry.get()))
    #  rollno = (int(rollnoEntry.get()))
    # Gives error in line 78 , unrecog tokenn
    rollnoEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_school + ", " + STUDENT_ADDRESS + ", " +
                       STUDENT_ROLLNO + " ) VALUES ( '"
                       + username + "', '" + schoolName + "', '" +
                       address + "', " + str(rollno) + " ); ")
    connection.commit()
    #messagebox.showinfo("Success", "Data Saved Successfully."))


def destroyRootWindow():
    root.destroy()
    secondWindow = tk.Tk()

    secondWindow.title("Student Database")

    appLabel = tk.Label(secondWindow, text="Student Database System",
                        fg="#06a099", width=45)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="School Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Roll Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()

button = tk.Button(root, text="Take input", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=30)

displayButton = tk.Button(root, text="Display result", command=lambda :destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()