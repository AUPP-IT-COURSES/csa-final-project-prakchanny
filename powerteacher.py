import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry

class StudentRecordEditor:
    def __init__(self, master):
        self.master = master
        self.master.title("Student Record Editor")

        # Student data
        self.students = [
            {"id": 101, "name": "Bean Sarem", "grade": "B", "attendance": "a","assignments": {"Math": "A", "English": "A", "Science": "C", "Social Studies": "B"}},
            {"id": 201, "name": "Chek Chantrea", "grade": "A", "attendance": "p", "assignments": {"Math": "A", "English": "B", "Science": "A", "Social Studies": "A"}},
            {"id": 301, "name": "Larch Chanminea", "grade": "A", "attendance": "p", "assignments":{"Math": "A", "English": "A", "Science": "A", "Social Studies": "A"}},
            {"id": 401, "name": "Hun Ellen", "grade": "B", "attendance": "p","assignments":{"Math": "B", "English": "B", "Science": "C", "Social Studies": "B"}},
            {"id": 501, "name": "Pa Sampoas", "grade": "A", "attendance": "a","assignments":{"Math": "A", "English": "B","Science": "A","Social Studies": "A"}},
            {"id": 601, "name": "Phann Sophairath", "grade": "A", "attendance": "p","assignments":{"Math": "A", "English": "A","Science": "A","Social Studies": "B"}},
            {"id": 701, "name": "Sao Samuth", "grade": "C", "attendance": "a","assignments":{"Math": "B", "English": "C","Science": "D","Social Studies": "C"}},
            {"id": 801, "name": "Tek Monika", "grade": "B", "attendance": "p","assignments":{"Math": "A", "English": "A","Science": "B","Social Studies": "C"}},
            {"id": 901, "name": "Tha Chantrea", "grade": "C", "attendance": "a","assignments":{"Math": "C", "English": "C","Science": "C","Social Studies": "C"}}
        ]

        # Create and configure notebook
        self.notebook = ttk.Notebook(master)

        self.grades_tab = ttk.Frame(self.notebook)
        self.assignments_tab = ttk.Frame(self.notebook)
        self.attendance_tab = ttk.Frame(self.notebook)

        self.notebook.add(self.grades_tab, text=" Overall Grades")
        self.notebook.add(self.assignments_tab, text="Detailed Grades")
        self.notebook.add(self.attendance_tab, text="Attendance")

        self.notebook.pack(expand=True, fill="both")

        # Grades tab
        self.create_grades_tab()

        # Assignments tab
        self.create_detailed_grade_tab()

        # Attendance tab
        self.create_attendance_tab()

    def create_grades_tab(self):
        self.grades_label = ttk.Label(self.grades_tab, text="Edit Grades")
        self.grades_label.grid(row=0, column=0, pady=10)

        self.grades_treeview = ttk.Treeview(self.grades_tab, columns=("ID", "Name", "Grade"), show="headings")
        self.grades_treeview.heading("ID", text="ID")
        self.grades_treeview.heading("Name", text="Name")
        self.grades_treeview.heading("Grade", text="Grade")

        for student in self.students:
            self.grades_treeview.insert("", "end", values=(student["id"], student["name"], student["grade"]))

        self.grades_treeview.grid(row=1, column=0, padx=10)

    def update_grade(self):
        selected_item = self.grades_treeview.selection()
        if selected_item:
            student_id = self.grades_treeview.item(selected_item)["values"][0]
            new_grade = self.grade_entry.get()

            # Update student data
            self.students[student_id - 1]["grade"] = new_grade

            # Update Treeview
            self.grades_treeview.item(selected_item, values=(student_id, self.students[student_id - 1]["name"], new_grade))

    def create_detailed_grade_tab(self):

        self.subject_label = ttk.Label(self.assignments_tab, text="Subject:")
        self.subject_label.grid(row=1, column=0, pady=10)
       
        self.subject_var = tk.StringVar()
        self.subject_dropdown = ttk.Combobox(self.assignments_tab, textvariable=self.subject_var, values=["Math", "English", "Science", "Social Studies"])  # Add more subjects as needed
        self.subject_dropdown.grid(row=1, column=1, pady=10)

        self.assignments_treeview = ttk.Treeview(self.assignments_tab, columns=("ID", "Name", "Assignment"), show="headings")
        self.assignments_treeview.heading("ID", text="ID")
        self.assignments_treeview.heading("Name", text="Name")
        self.assignments_treeview.heading("Assignment", text="Grade")

        self.subject_dropdown.bind("<<ComboboxSelected>>", self.update_assignments_treeview)

        self.assignments_treeview.grid(row=3, column=0, padx=10, columnspan=2)

        self.update_assignments_treeview()

        self.assignment_label = ttk.Label(self.assignments_tab, text="New Grade:")
        self.assignment_label.grid(row=2, column=0, pady=5)
        self.assignment_entry = ttk.Entry(self.assignments_tab)
        self.assignment_entry.grid(row=2, column=1, pady=5)

        self.update_assignment_button = ttk.Button(self.assignments_tab, text="Update Grade", command=self.update_assignment)
        self.update_assignment_button.grid(row=4, column=0, columnspan=2, pady=10)
        

    def update_assignments_treeview(self, event=None):
        selected_subject = self.subject_var.get()
        self.assignments_treeview.delete(*self.assignments_treeview.get_children())

        for student in self.students:
            student_id = student["id"]
            student_name = student["name"]
            assignment = student["assignments"].get(selected_subject, "")
            self.assignments_treeview.insert("", "end", values=(student_id, student_name, assignment))

    def update_assignment(self):
        selected_item = self.assignments_treeview.selection()
        if selected_item:
            student_id = self.assignments_treeview.item(selected_item)["values"][0]
            new_assignment = self.assignment_entry.get()
            selected_subject = self.subject_var.get()

            # Update student data
            self.students[student_id - 1]["assignments"][selected_subject] = new_assignment

            # Update Treeview
            self.assignments_treeview.item(selected_item, values=(student_id, self.students[student_id - 1]["name"], new_assignment))
            

    def create_attendance_tab(self):
        self.attendance_label = ttk.Label(self.attendance_tab, text="Edit Attendance")
        self.attendance_label.grid(row=0, column=0, pady=10)
# =--------------------------------create the attendance drop down------------------
        # self.attendance_label = ttk.Label(self.attendance_tab, text="Date:")
        # self.attendance_label.grid(row=1, column=0, pady=10)

        # Use DateEntry widget for more convenient date choosing
        self.attendance_var = tk.StringVar()
        self.attendance_entry = DateEntry(self.attendance_tab, textvariable=self.attendance_var, width=12, background="darkblue", foreground="white", borderwidth=2, values=["12/1/23", "12/2/23","12/3/23"])
        self.attendance_entry.grid(row=1, column=1, pady=10)

        self.update_attendance_button = ttk.Button(self.attendance_tab, text="Update Attendance", command=self.update_attendance)
        self.update_attendance_button.grid(row=3, column=0, columnspan=2, pady=10)


        self.attendance_treeview = ttk.Treeview(self.attendance_tab, columns=("ID", "Name", "Attendance"), show="headings")
        self.attendance_treeview.heading("ID", text="ID")
        self.attendance_treeview.heading("Name", text="Name")
        self.attendance_treeview.heading("Attendance", text="Attendance")

        for student in self.students:
            self.attendance_treeview.insert("", "end", values=(student["id"], student["name"], student["attendance"]))

        self.attendance_treeview.grid(row=1, column=0, padx=10)

        self.attendance_label = ttk.Label(self.attendance_tab, text="New Attendance:")
        self.attendance_label.grid(row=2, column=0, pady=5)
        self.attendance_entry = ttk.Entry(self.attendance_tab)
        self.attendance_entry.grid(row=2, column=1, pady=5)

        self.update_attendance_button = ttk.Button(self.attendance_tab, text="Update Attendance", command=self.update_attendance)
        self.update_attendance_button.grid(row=3, column=0, columnspan=2, pady=10)

    def update_attendance(self):
        selected_item = self.attendance_treeview.selection()
        if selected_item:
            student_id = self.attendance_treeview.item(selected_item)["values"][0]
            new_attendance = self.attendance_entry.get()

            # Update student data
            self.students[student_id - 1]["attendance"] = new_attendance

            # Update Treeview
            self.attendance_treeview.item(selected_item, values=(student_id, self.students[student_id - 1]["name"], new_attendance))

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRecordEditor(root)
    root.mainloop()
