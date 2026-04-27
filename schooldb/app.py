from tkinter import ttk, Tk, Frame, Label, LEFT, CENTER, VERTICAL, RIGHT, BOTH, Y
from dbhelper import *

class StudentUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("STUDENTS")
        self.root.resizable(False, False)
        self.centerwindow(900, 450)
        
        # Main container frame for side-by-side layout
        self.main_frame = Frame(self.root)
        self.main_frame.pack(fill=BOTH, expand=True, padx=15, pady=15)
        
        # Initialize GUI components side by side
        self.studentlist()
        self.studentform()
        self.load_students()
        
        self.root.mainloop()
        
    def centerwindow(self, width:int, height:int) -> None:
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def studentform(self) -> None:
        # Form Frame - RIGHT SIDE
        form_frame = Frame(self.main_frame, padx=20, pady=20)
        form_frame.pack(side=RIGHT, fill=Y)
        
        # Labels and Entries (vertical layout - single column)
        Label(form_frame, text="ID No:", font=('Arial', 10)).grid(row=0, column=0, sticky=W, pady=8)
        self.idno_entry = Entry(form_frame, font=('Arial', 10), width=28)
        self.idno_entry.grid(row=0, column=1, padx=15, pady=8)
        
        Label(form_frame, text="Last Name:", font=('Arial', 10)).grid(row=1, column=0, sticky=W, pady=8)
        self.lastname_entry = Entry(form_frame, font=('Arial', 10), width=28)
        self.lastname_entry.grid(row=1, column=1, padx=15, pady=8)
        
        Label(form_frame, text="First Name:", font=('Arial', 10)).grid(row=2, column=0, sticky=W, pady=8)
        self.firstname_entry = Entry(form_frame, font=('Arial', 10), width=28)
        self.firstname_entry.grid(row=2, column=1, padx=15, pady=8)
        
        Label(form_frame, text="Course:", font=('Arial', 10)).grid(row=3, column=0, sticky=W, pady=8)
        self.course_entry = Entry(form_frame, font=('Arial', 10), width=28)
        self.course_entry.grid(row=3, column=1, padx=15, pady=8)
        
        Label(form_frame, text="Level:", font=('Arial', 10)).grid(row=4, column=0, sticky=W, pady=8)
        self.level_entry = Entry(form_frame, font=('Arial', 10), width=28)
        self.level_entry.grid(row=4, column=1, padx=15, pady=8)
    
    def studentlist(self) -> None:
        # Table Frame - LEFT SIDE
        table_frame = Frame(self.main_frame)
        table_frame.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Create Treeview using self.tv as instructed
        columns = ('idno', 'lastname', 'firstname', 'course', 'level')
        self.tv = ttk.Treeview(table_frame, columns=columns, show='headings')
        
        # Define headings using self.tv
        self.tv.heading('idno', text='ID No')
        self.tv.heading('lastname', text='Last Name')
        self.tv.heading('firstname', text='First Name')
        self.tv.heading('course', text='Course')
        self.tv.heading('level', text='Level')
        
        # Set column widths
        self.tv.column('idno', width=100, anchor=CENTER)
        self.tv.column('lastname', width=150)
        self.tv.column('firstname', width=150)
        self.tv.column('course', width=120)
        self.tv.column('level', width=80, anchor=CENTER)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(table_frame, orient=VERTICAL, command=self.tv.yview)
        self.tv.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=RIGHT, fill=Y)
        
        self.tv.pack(fill=BOTH, expand=True)
        
        # Bind row select event
        self.tv.bind('<<TreeviewSelect>>', self.on_row_select)
    
    def load_students(self) -> None:
        # Clear existing items
        for item in self.tv.get_children():
            self.tv.delete(item)
        
        # Get all students from database
        students = getall("students")
        
        # Insert into treeview
        for student in students:
            self.tv.insert('', END, values=(
                student['idno'],
                student['lastname'],
                student['firstname'],
                student['course'],
                student['level']
            ))
    
    def on_row_select(self, event) -> None:
        # Clear form first
        self.clear_form()
        
        # Get selected item
        selected = self.tv.selection()
        if selected:
            item = self.tv.item(selected[0])
            values = item['values']
            
            # Load values into form entries
            self.idno_entry.insert(0, values[0])
            self.lastname_entry.insert(0, values[1])
            self.firstname_entry.insert(0, values[2])
            self.course_entry.insert(0, values[3])
            self.level_entry.insert(0, values[4])
    
    def clear_form(self) -> None:
        # Clear all entry fields
        self.idno_entry.delete(0, END)
        self.lastname_entry.delete(0, END)
        self.firstname_entry.delete(0, END)
        self.course_entry.delete(0, END)
        self.level_entry.delete(0, END)
    
def main() -> None:
    StudentUI()

if __name__ == "__main__":
    main()