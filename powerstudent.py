import tkinter as tk
from tkinter import ttk

# Student data
students = [
    {"id": 101, "name": "Bean Sarem", "grade": "A", "attendance": "a", "assignments": {"Math": "A", "English": "A", "Science": "C", "Social Studies": "B"}},
    {"id": 201, "name": "Chek Chantrea", "grade": "B", "attendance": "p", "assignments": {"Math": "A", "English": "B", "Science": "A", "Social Studies": "A"}},
    {"id": 301, "name": "Larch Chanminea", "grade": "A", "attendance": "p", "assignments": {"Math": "A", "English": "A", "Science": "A", "Social Studies": "A"}},
    {"id": 401, "name": "Hun Ellen", "grade": "A", "attendance": "p", "assignments": {"Math": "A", "English": "B", "Science": "C", "Social Studies": "B"}},
    {"id": 501, "name": "Pa Sampoas", "grade": "C", "attendance": "a", "assignments": {"Math": "A", "English": "B", "Science": "A", "Social Studies": "A"}},
    {"id": 601, "name": "Phann Sophairath", "grade": "A", "attendance": "p", "assignments": {"Math": "A", "English": "A", "Science": "A", "Social Studies": "B"}},
    {"id": 701, "name": "Sao Samuth", "grade": "C", "attendance": "a", "assignments": {"Math": "A", "English": "C", "Science": "D", "Social Studies": "A"}},
    {"id": 801, "name": "Tek Monika", "grade": "A", "attendance": "p", "assignments": {"Math": "A", "English": "A", "Science": "B", "Social Studies": "C"}},
    {"id": 901, "name": "Tha Chantrea", "grade": "C", "attendance": "a", "assignments": {"Math": "A", "English": "B", "Science": "A", "Social Studies": "A"}},
]

class StudentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Grades App")
        root.geometry('925x500+300+200')

        # Login frame
        self.login_frame = ttk.Frame(self.root, padding="10")
        self.login_frame.grid(row=0, column=0, sticky="nsew")

        # Labels and Entry widgets for login
        ttk.Label(self.login_frame, text="Name:").grid(row=0, column=0, sticky="e")
        ttk.Label(self.login_frame, text="ID:").grid(row=1, column=0, sticky="e")
        self.name_entry = ttk.Entry(self.login_frame)
        self.id_entry = ttk.Entry(self.login_frame)
        self.name_entry.grid(row=0, column=1, sticky="w")
        self.id_entry.grid(row=1, column=1, sticky="w")

        # Login button
        ttk.Button(self.login_frame, text="Login", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        name = self.name_entry.get()
        student_id = int(self.id_entry.get())

        # Search for the student
        student = next((s for s in students if s["name"] == name and s["id"] == student_id), None)

        if student:
            # Destroy login frame
            self.login_frame.destroy()

            # Display student grades
            self.display_grades(student)
        else:
            # Display error message for invalid login
            ttk.Label(self.login_frame, text="Invalid login. Please try again.", foreground="red").grid(row=3, column=0, columnspan=2)

    def display_grades(self, student):
        # Grades frame
        self.grades_frame = ttk.Frame(self.root, padding="10")
        self.grades_frame.grid(row=0, column=0, sticky="nsew")

        # Table header
        header = ["Subject", "Grade"]
        for col, h in enumerate(header):
            ttk.Label(self.grades_frame, text=h, font=("Helvetica", 10, "bold")).grid(row=0, column=col, padx=5, pady=5)

        # Display student data in the table
        for row, (subject, grade) in enumerate(student["assignments"].items(), start=1):
            ttk.Label(self.grades_frame, text=subject).grid(row=row, column=0, padx=5, pady=5)
            ttk.Label(self.grades_frame, text=grade).grid(row=row, column=1, padx=5, pady=5)

# Main loop
if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()
