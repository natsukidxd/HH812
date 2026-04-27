from tkinter import Tk, ttk, messagebox, Label, Entry
from dbhelper import *
import tkinter as tk

class StudentUI:
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("STUDENTS")
        self.root.resizable(False, False)
        self.centerwindow(700, 500)
        self.root.mainloop()
        
    def centerwindow(self, width:int, height:int) -> None:
        screen_width = self.root.winfo_screenwidth()
        self.root.geometry(f"{width}x{height}")
    
    def studentlist(self) -> None:
        pass
    
    def studentform(self) -> None:
        pass
    
def main() -> None:
    pass