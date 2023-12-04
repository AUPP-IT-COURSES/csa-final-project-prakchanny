from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

root = Tk()
root.title('Login Form')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

def signin():
    # Check if the user is a student or a teacher
    user_role = role_var.get()

    if user_role == "student":
        student_login()
    elif user_role == "teacher":
        teacher_login()
    else:
        messagebox.showerror("Invalid Role", "Please select a role.")

def student_login():
    username = user.get()
    password = code.get()

    # Check if the username and password are correct for a student
    # Add your student login logic here
    # For now, using a dummy condition
    if username == "student" and password == "1111":
        def execute_python_file(file_path):
            try:
                with open(file_path, 'r') as file:
                    python_code = file.read()
                exec(python_code)
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
        file_path ='powerstudent.py'
        execute_python_file(file_path)  
    else:
        messagebox.showerror("Invalid", "Invalid username or password for student.")

def teacher_login():
    username = user.get()
    password = code.get()

    # Check if the username and password are correct for a teacher
    # Add your teacher login logic here
    # For now, using a dummy condition
    if username == "admin" and password == "9999":
        def execute_python_file(file_path):
            try:
                with open(file_path, 'r') as file:
                    python_code = file.read()
                exec(python_code)
            except FileNotFoundError:
                print(f"Error: The file '{file_path}' does not exist.")
        file_path ='powerteacher.py'
        execute_python_file(file_path)  
    else:
        messagebox.showerror("Invalid", "Invalid username or password for teacher.")

img = PhotoImage(file='login.png')
Label(root, image=img, bg='white').place(x=-25, y=0)

frame = Frame(root, width=350, height=350, bg='white')
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading.place(x=100, y=0)

# Role selection
role_var = StringVar()
role_var.set("student")  # Default to student
student_radio = Radiobutton(frame, text="Student", variable=role_var, value="student", bg='white')
teacher_radio = Radiobutton(frame, text="Teacher", variable=role_var, value="teacher", bg='white')
student_radio.place(x=30, y=40)
teacher_radio.place(x=130, y=40)

# --------------------------user------------------------
def on_enter(e):
    user.delete(0, 'end')

def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# ---------------------------password----------------------
def on_enter(e):
    code.delete(0, 'end')

def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')


code = Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)
# ----------------------------------------------------------

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft Yahei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8')
sign_up.place(x=215, y=270)

root.mainloop()
