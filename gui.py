import tkinter as tk
from tkinter import filedialog as fd
import matplotlib.pyplot as plt
import matplotlib as mpl
from numpy import linspace, pi
mpl.use("TkAgg")
from generate_transfer_function import TransferFunction, compute_data, invert, savetocsv, load_from_file

class mainGUI:
    def __init__(self, master):
        self.master = master
        master.title("TFM Transfer Function GUI")
        self.label = tk.Label(master, text="Generate Transfer Function")
        self.label.grid(row=0,column=2)

        # Button and Entry for Loading File
        self.load_file = tk.IntVar()
        self.file_bool = tk.Checkbutton(master, text="Load from File", variable = self.load_file)
        self.file_bool.grid(column=1)
        
        self.greet_button = tk.Button(master, text="File", command=self.getfile)
        self.greet_button.grid(column=1)

        self.lb1 = tk.StringVar()
        self.lb1.set("No File Loaded")
        self.file_entry = tk.Label(master, textvariable=self.lb1)
        self.file_entry.grid(column=1)


        # Entries for Frequency Values
        self.start_entry = tk.Entry(master)
        self.start_entry.grid(column=2)
        self.start_entry.insert(0,"Starting Freq")
        self.end_entry = tk.Entry(master)
        self.end_entry.grid(column=2)
        self.end_entry.insert(0,"Ending Freq")
        self.step_entry = tk.Entry(master)
        self.step_entry.grid(column=2)
        self.step_entry.insert(0,"Step Size")

        self.output_file = tk.Entry(master)
        self.output_file.grid(column=2,pady=5)
        self.output_file.insert(0, "Output Path")

        # Inputs for Amp/Phase functions
        self.amp_l = tk.Label(master, text="A(f) = ")
        self.amp_l.grid(column=2,row=1,sticky='E')
        self.amp_in = tk.Entry(master)
        self.amp_in.grid(column=3,row=1,sticky='W')
        self.amp_in.insert(0, "f")

        self.phi_l = tk.Label(master, text="Phi(f) = ")
        self.phi_l.grid(column=2,row=2,sticky='E')
        self.phi_in = tk.Entry(master)
        self.phi_in.grid(column=3,row=2,sticky='W')
        self.phi_in.insert(0, "0")

        # Compute button
        self.go_button = tk.Button(master, text="Compute", command=self.compute)
        self.go_button.grid(column=2)

        # Graphs
        fig = plt.Figure(figsize=(8,3))
        fig.patch.set_facecolor('#efefef')

        self.ax1 = fig.add_subplot(1,2,1)
        self.ax2 = fig.add_subplot(1,2,2)
        self.ax1.set_title("Inverse Amplitude Function")
        self.ax1.set_xlabel("Frequency (Hz)")
        self.ax1.set_ylabel("Amplitude (relative voltage)")
        self.ax2.set_title("Inverse Phase Function")
        self.ax2.set_xlabel("Frequency (Hz)")
        self.ax2.set_ylabel("Phase (radians)")
        self.canvas = mpl.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(column=1, columnspan=3, pady=5)
        

    def amplitude_function(self,f):
        string = self.amp_in.get()
        return eval(string)

    def phase_function(self,f):
        string = self.phi_in.get()
        phi = eval(string)
        phi = phi%(2*pi)
        return phi
        
    def getfile(self):
        self.path = fd.askopenfilename()
        self.lb1.set(self.path)

    def makegraph(self, data):
        steps = int((self.end_freq - self.start_freq)/self.step_size + 1)
        freq_range = linspace(self.start_freq, self.end_freq, steps)
        self.ax1.clear()
        self.ax2.clear()
        self.ax1.plot(freq_range, data[:,0],label="Inverse Amplitude")
        self.ax2.plot(freq_range, data[:,1],label="Inverse Phase")

        self.canvas.draw()
        self.toolbar.update()


    def a1(self,f):
        return 1
    def p0(self,f):
        return 0

    def compute(self):
        try:
            self.start_freq = int(self.start_entry.get())
            self.end_freq = int(self.end_entry.get())
            self.step_size = int(self.step_entry.get())
            if self.end_freq < self.start_freq:
                error = tk.Toplevel()
                error.title("Error")

                msg = tk.Message(error, text="End frequency must be larger then starting requency")
                msg.pack()
                
        except ValueError:
            print("Input Error")
            error = tk.Toplevel()
            error.title("Error")

            msg = tk.Message(error, text="Frequencies must be numbers in Hz \n")
            msg.pack()
            return False

    
        file = self.output_file.get()

        boolean = self.load_file.get()
        if not boolean:
            self.ampf = self.amplitude_function
            self.phif = self.phase_function
        else:
            self.ampf, self.phif = load_from_file(self.path)
            
        data = compute_data(self.end_freq, self.start_freq, self.step_size, self.ampf, self.phif)
        data = invert(data)
     
            
        try:
            savetocsv(file, data)
        except:
            error = tk.Toplevel()
            error.title("Error")
            msg = tk.Message(error, text="An error occured saving the file.")
            msg.pack()
            return False

        self.makegraph(data)
        return True

root = tk.Tk()
my_gui = mainGUI(root)
root.mainloop()
