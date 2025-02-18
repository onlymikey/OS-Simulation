import tkinter as tk
from tkinter import ttk
from Views.processes import ProcessesUI
from Views.lot import BatchUI

class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Churumbilito OS")
        self.master.geometry("1366x768")

        # Create a notebook (tabs)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill="both", expand=True)

        # Create frames for each tab
        self.processes_frame = ttk.Frame(self.notebook)
        self.batches_frame = ttk.Frame(self.notebook)

        # Add frames to notebook
        self.notebook.add(self.processes_frame, text="Procesos")
        self.notebook.add(self.batches_frame, text="Lotes")

        # Initialize UI
        self.processes_ui = ProcessesUI(self.processes_frame, self)
        self.batches_ui = BatchUI(self.batches_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
