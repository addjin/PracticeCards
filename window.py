import asyncio
from ast import Pass
import tkinter as tk
from tkinter import VERTICAL, ttk

testtext = "sdf\ns\nd\nf\ns\nd\nf\ns\nd\nfsdf\ns\nd\nf\ns\nd\nf\ns\nd\nfsdf\ns\nd\nf\ns\nd\nf\ns\nd\nfsdf\ns\nd\nf\ns\nd\nf\ns\nd\nf"

class Window(tk.Tk):
    def __init__(self):
        # self.loop = loop
        self.root = tk.Tk()
        self.root.title("Practice Cards")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.root.grid_columnconfigure(0, weight=10)
        self.root.grid_columnconfigure(1, weight=10)
        self.root.grid_columnconfigure(2, weight=10)
        self.root.grid_columnconfigure(3, weight=1)
        self.root.grid_rowconfigure(5, weight=1)

        self.app_title_label = tk.Label(
            self.root, text="Practice Cards", anchor=tk.CENTER, font=("Helvetica", 15))
        self.app_title_label.grid(row=0, column=0, columnspan=4)
        self.text = tk.Text(self.root, width=30)
        # self.text.insert("0.2", testtext)
        self.text.grid(row=1, column=3, padx=5, sticky=tk.EW)
        self.scrollbar = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.text.yview)
        self.scrollbar.grid(row=1, column=4, sticky=tk.NS)
        self.text['yscrollcommand'] = self.scrollbar.set


window = Window()

window.root.mainloop()
