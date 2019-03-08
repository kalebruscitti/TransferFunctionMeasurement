import tkinter as tk
from tkinter import filedialog as fd

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = tk.Label(master, text="Generate Transfer Function")
        self.label.pack()

        self.greet_button = tk.Button(master, text="File", command=self.getfile)
        self.greet_button.pack()

        self.close_button = tk.Button(master, text="Close", command=master.quit)
        self.close_button.pack()

        self.lb1 = tk.StringVar()
        self.lb1.set("No File Loaded")
        self.file_entry = tk.Label(master, textvariable=self.lb1)
        self.file_entry.pack()

        self.start_entry = tk.Entry(master)
        self.start_entry.pack()
        self.start_entry.insert(0,"Starting Freq")
        self.end_entry = tk.Entry(master)
        self.end_entry.pack()
        self.end_entry.insert(0,"Ending Freq")
        self.step_entry = tk.Entry(master)
        self.step_entry.pack()
        self.step_entry.insert(0,"Step Size")

    def getfile(self):
        path = fd.askopenfilename()
        self.lb1.set(path)
        print(path)

root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
