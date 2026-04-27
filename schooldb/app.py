from tkinter import Tk, ttk, messagebox, Label, Frame, Entry
from dbhelper import *


class StudentUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("STUDENTS")
        self.root.resizable(False, False)
        self.centerwindow(900, 250)

        self.main_frame = Frame(self.root)
        self.main_frame.pack(padx=15, pady=15)

        self.studentlist()
        self.studentform()
        self.load_students()

        self.root.mainloop()

    def centerwindow(self, width: int, height: int) -> None:
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def studentform(self) -> None:
        form_frame = Frame(self.main_frame, padx=20, pady=20)
        form_frame.pack(side="right", fill="y")

        Label(form_frame, text="ID No:").grid(row=0, column=0, sticky="w", pady=8)
        self.idno_entry = Entry(form_frame, width=28)
        self.idno_entry.grid(row=0, column=1, padx=15, pady=8)

        Label(form_frame, text="Last Name:").grid(row=1, column=0, sticky="w", pady=8)
        self.lastname_entry = Entry(form_frame, width=28)
        self.lastname_entry.grid(row=1, column=1, padx=15, pady=8)

        Label(form_frame, text="First Name:").grid(row=2, column=0, sticky="w", pady=8)
        self.firstname_entry = Entry(form_frame, width=28)
        self.firstname_entry.grid(row=2, column=1, padx=15, pady=8)

        Label(form_frame, text="Course:").grid(row=3, column=0, sticky="w", pady=8)
        self.course_entry = Entry(form_frame, width=28)
        self.course_entry.grid(row=3, column=1, padx=15, pady=8)

        Label(form_frame, text="Level:").grid(row=4, column=0, sticky="w", pady=8)
        self.level_entry = Entry(form_frame, width=28)
        self.level_entry.grid(row=4, column=1, padx=15, pady=8)

    def studentlist(self) -> None:
        table_frame = Frame(self.main_frame)
        table_frame.pack(side="left", fill="both", expand=True)

        columns = ("idno", "lastname", "firstname", "course", "level")
        self.tv = ttk.Treeview(table_frame, columns=columns, show="headings")

        self.tv.heading("idno", text="ID No")
        self.tv.heading("lastname", text="Last Name")
        self.tv.heading("firstname", text="First Name")
        self.tv.heading("course", text="Course")
        self.tv.heading("level", text="Level")

        self.tv.column("idno", width=100)
        self.tv.column("lastname", width=150)
        self.tv.column("firstname", width=150)
        self.tv.column("course", width=120)
        self.tv.column("level", width=80)

        self.tv.pack(fill="both", expand=True)

        self.tv.bind("<<TreeviewSelect>>", self.on_row_select)

    def load_students(self) -> None:
        for item in self.tv.get_children():
            self.tv.delete(item)

        students = getall("students")

        for student in students:
            self.tv.insert(
                "",
                "end",
                values=(
                    student["idno"],
                    student["lastname"],
                    student["firstname"],
                    student["course"],
                    student["level"],
                ),
            )

    def on_row_select(self, event) -> None:
        self.clear_form()

        selected = self.tv.selection()
        if selected:
            item = self.tv.item(selected[0])
            values = item["values"]

            self.idno_entry.insert(0, values[0])
            self.lastname_entry.insert(0, values[1])
            self.firstname_entry.insert(0, values[2])
            self.course_entry.insert(0, values[3])
            self.level_entry.insert(0, values[4])

    def clear_form(self) -> None:
        self.idno_entry.delete(0, "end")
        self.lastname_entry.delete(0, "end")
        self.firstname_entry.delete(0, "end")
        self.course_entry.delete(0, "end")
        self.level_entry.delete(0, "end")


def main() -> None:
    StudentUI()


if __name__ == "__main__":
    main()
