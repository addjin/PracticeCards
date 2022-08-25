import asyncio
from fileinput import filename
from card import Deck
from ast import Pass
import time
import os
import pathlib
import tkinter as tk
from tkinter import ttk, filedialog
from utilities import *

testtext = "sdf\ns\nd\nf\ns\nd\nf\ns\nd\nfsdf\ns\nd\nf\ns\nd\nf\ns\nd\nfsdf\ns\nd\nf\ns\nd\nf\ns\nd\nfsdf\ns\nd\nf\ns\nd\nf\ns\nd\nf"

decks = {}


class MainWindow(tk.Tk):
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        self.root = tk.Tk()
        self.root.title("Practice Cards")
        self.root.geometry("500x400")
        self.root.resizable(False, False)

        self.root.grid_columnconfigure(0, weight=10)
        self.root.grid_columnconfigure(1, weight=10)
        self.root.grid_columnconfigure(2, weight=10)
        self.root.grid_columnconfigure(3, weight=1)

        for i in range(11):
            self.root.grid_rowconfigure(i, weight=1)
        # self.root.grid_rowconfigure(0, weight=2)

        self.app_title_label = tk.Label(
            self.root, text="Practice Cards", font=("Helvetica", 15))
        self.app_title_label.grid(
            row=0, column=0, columnspan=4, pady=10, sticky=tk.W)

        self.load_button = tk.Button(
            self.root, text="Load", width=10, command=self.loadbutton_click)
        self.load_button.grid(row=1, column=0, padx=3, sticky=tk.NW, pady=0)

        self.start_button = tk.Button(
            self.root, text="Start", width=10, command=self.startbutton_click)
        self.start_button.grid(row=2, column=0, padx=3, sticky=tk.NW, pady=1)

        self.deck_listbox = tk.Listbox(self.root)
        self.deck_listbox.grid(row=1, column=1, rowspan=5, columnspan=2,
                               padx=1, pady=1, sticky=tk.NSEW)
        self.deck_listbox_scrollbar = ttk.Scrollbar(
            self.root, orient=tk.VERTICAL, command=self.deck_listbox.yview)
        self.deck_listbox_scrollbar.grid(
            row=1, column=4, rowspan=5, sticky=tk.NS, pady=1)
        # self.deck_listbox_scrollbar['yscrollcommand'] = self.deck_listbox.yview_scroll

        self.infotextbox = tk.Text(self.root, state='disabled')
        # self.infotextbox.insert("0.2", testtext)
        self.infotextbox.grid(
            row=6, column=0, sticky=tk.EW, rowspan=4, columnspan=2, padx=1, pady=3)
        self.infotextbox_scrollbar = ttk.Scrollbar(
            self.root, orient=tk.VERTICAL, command=self.infotextbox.yview)
        self.infotextbox_scrollbar.grid(
            row=6, column=4, rowspan=4, sticky=tk.NS, pady=1)
        self.infotextbox['yscrollcommand'] = self.infotextbox_scrollbar.set

        self.__append_to_infotextbox("Program started.")

    def __append_to_infotextbox(self, message):
        self.infotextbox['state'] = 'normal'
        timestamp = "[" + get_time() + "] "
        message = timestamp + message + "\n"
        self.infotextbox.insert("0.0", message)
        self.infotextbox['state'] = 'disabled'

    def loadbutton_click(self):
        files = filedialog.askopenfilenames()
        if files == "":
            self.__append_to_infotextbox("Deck loading cancelled.")
            return False
        else:
            for file in files:
                deckname = os.path.basename(file)
                if deckname in decks:
                    deckname
                newdeck = Deck(deckName=deckname)
                if newdeck.read(file, infoCallback=self.__append_to_infotextbox):
                    if deckname in decks:
                        decks[deckname] = newdeck
                        self.__append_to_infotextbox(f"\"{newdeck.DeckName}\" added to deck list.")
                pass

        print(files)

    def startbutton_click(self):
        self.root.withdraw()
        print("Test")


window = MainWindow()

window.root.mainloop()
