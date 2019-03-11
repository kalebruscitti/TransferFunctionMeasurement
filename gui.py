import tkinter as tk
from tkinter import filedialog as fd
from generate_transfer_function import TransferFunction, compute_data, invert, savetocsv, load_from_file

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("TFM Transfer Function GUI")
        self.label = tk.Label(master, text="Generate Transfer Function")
        self.label.pack()

        self.greet_button = tk.Button(master, text="File", command=self.getfile)
        self.greet_button.pack()

        self.go_button = tk.Button(master, text="Compute", command=self.compute)
        self.go_button.pack()

        self.lb1 = tk.StringVar()
        self.lb1.set("No File Loaded")
        self.file_entry = tk.Label(master, textvariable=self.lb1)
        self.file_entry.pack()

        self.load_file = tk.IntVar()
        self.file_bool = tk.Checkbutton(master, text="Load from File", variable = self.load_file)
        self.file_bool.pack()

        self.start_entry = tk.Entry(master)
        self.start_entry.pack()
        self.start_entry.insert(0,"Starting Freq")
        self.end_entry = tk.Entry(master)
        self.end_entry.pack()
        self.end_entry.insert(0,"Ending Freq")
        self.step_entry = tk.Entry(master)
        self.step_entry.pack()
        self.step_entry.insert(0,"Step Size")

        self.output_file = tk.Entry(master)
        self.output_file.pack()
        self.output_file.insert(0, "Output Path")

    def getfile(self):
        path = fd.askopenfilename()
        self.lb1.set(path)
        self.ampf, self.phif = load_from_file(path)

    def compute(self):
        try:
            self.start_freq = int(self.start_entry.get())
            self.end_freq = int(self.end_entry.get())
            self.step_size = int(self.step_entry.get())
        except:
            print("Input Error")

        file = self.output_file.get()
        
        data = compute_data(self.end_freq, self.start_freq, self.step_size, self.load_file, self.ampf, self.phif)
        data = invert(data)
        savetocsv(file, data)
    

root = tk.Tk()
my_gui = MyFirstGUI(root)
root.mainloop()
