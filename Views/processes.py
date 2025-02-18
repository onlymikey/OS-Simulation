import tkinter as tk
from tkinter import ttk
from Controllers.processes_controller import ProcessController
from tkinter import messagebox
import uuid

class ProcessesUI:
    def __init__(self, master, app):
        self.master = master
        self.app = app
        self.processes_controller = ProcessController()  # Inicializar el controlador
        # Grid configuration
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=2)
        self.master.columnconfigure(2, weight=1)

        # Label and Spinbox for "Procesos por lote"
        self.lot_processes_label = ttk.Label(self.master, text="Procesos por lote:")
        self.lot_processes_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.lot_processes_spinbox = ttk.Spinbox(self.master, from_=1, to=100, width=10)
        self.lot_processes_spinbox.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        # Label and entry for "Nombre del programa"
        self.program_name_label = ttk.Label(self.master, text="Nombre del programa:")
        self.program_name_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.program_name_entry = ttk.Entry(self.master)
        self.program_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Label and entry for "Tiempo estimado de ejecución"
        self.execution_time_label = ttk.Label(self.master, text="Tiempo estimado de ejecución (mm:ss):")
        self.execution_time_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.execution_time_entry = ttk.Entry(self.master)
        self.execution_time_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")
        self.execution_time_entry.insert(0, "00:00")  # Default value

        # Label, entry, and button for "Número de programa"
        self.program_number_label = ttk.Label(self.master, text="Número de programa:")
        self.program_number_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.program_number_entry = ttk.Entry(self.master, state="readonly")
        self.program_number_entry.grid(row=3, column=1, padx=(10, 5), pady=10, sticky="w")

        self.generate_button = ttk.Button(self.master, text="Generar", command=self.generate_uuid)
        self.generate_button.grid(row=3, column=1, padx=(5, 10), pady=10, sticky="e")  # Positioned next to Entry

        # Combobox for operation selection
        self.operation_label = ttk.Label(self.master, text="Operación:")
        self.operation_label.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.operation_combobox = ttk.Combobox(
            self.master,
            values=["Suma", "Resta", "Multiplicación", "División", "Residuo", "Potencia"],
            state="readonly"
        )
        self.operation_combobox.grid(row=4, column=1, padx=10, pady=10, sticky="w")
        self.operation_combobox.bind("<<ComboboxSelected>>", self.update_operation_fields)

        # Frame for operation inputs (updated dynamically)
        self.operation_inputs_frame = ttk.Frame(self.master)
        self.operation_inputs_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for Save and Cancel
        self.save_button = ttk.Button(self.master, text="Guardar", command=self.save_data)
        self.save_button.grid(row=6, column=0, padx=10, pady=20, sticky="e")

        self.cancel_button = ttk.Button(self.master, text="Cancelar", command=self.cancel_action)
        self.cancel_button.grid(row=6, column=1, padx=10, pady=20, sticky="w")

    def generate_uuid(self):
        # Generate a short UUID and insert it into the "Número de programa" field
        short_uuid = str(uuid.uuid4())[:8]  # Take the first 8 characters of the UUID
        self.program_number_entry.config(state="normal")  # Temporarily enable the entry
        self.program_number_entry.delete(0, tk.END)
        self.program_number_entry.insert(0, short_uuid)
        self.program_number_entry.config(state="readonly")  # Disable the entry again

    def update_operation_fields(self, event=None):
        # Clear the current inputs in the operation frame
        for widget in self.operation_inputs_frame.winfo_children():
            widget.destroy()

        # Get the selected operation
        operation = self.operation_combobox.get()

        # Create appropriate number of entry fields based on the operation
        if operation in ["Suma", "Resta", "Multiplicación", "División", "Residuo"]:
            ttk.Label(self.operation_inputs_frame, text="Dato 1:").grid(row=0, column=0, padx=5, pady=5)
            self.input1_entry = ttk.Entry(self.operation_inputs_frame)
            self.input1_entry.grid(row=0, column=1, padx=5, pady=5)

            ttk.Label(self.operation_inputs_frame, text="Dato 2:").grid(row=1, column=0, padx=5, pady=5)
            self.input2_entry = ttk.Entry(self.operation_inputs_frame)
            self.input2_entry.grid(row=1, column=1, padx=5, pady=5)

        elif operation == "Potencia":
            ttk.Label(self.operation_inputs_frame, text="Base:").grid(row=0, column=0, padx=5, pady=5)
            self.input1_entry = ttk.Entry(self.operation_inputs_frame)
            self.input1_entry.grid(row=0, column=1, padx=5, pady=5)

            ttk.Label(self.operation_inputs_frame, text="Exponente:").grid(row=1, column=0, padx=5, pady=5)
            self.input2_entry = ttk.Entry(self.operation_inputs_frame)
            self.input2_entry.grid(row=1, column=1, padx=5, pady=5)

    def save_data(self):
        # Retrieve data from fields
        lot_processes = self.lot_processes_spinbox.get()
        program_name = self.program_name_entry.get()
        execution_time = self.execution_time_entry.get()
        program_number = self.program_number_entry.get()
        operation = self.operation_combobox.get()
        input1 = self.input1_entry.get() if hasattr(self, "input1_entry") else None
        input2 = self.input2_entry.get() if hasattr(self, "input2_entry") else None

        # Validate data
        result = self.processes_controller.validate_process_data(lot_processes, program_name, execution_time, program_number, operation, input1, input2)

        if result['status']:
            messagebox.showinfo("Éxito", result['message'])
            self.cancel_action()
        else:
            messagebox.showerror("Error", result['message'])

    def cancel_action(self):
        # Clear all fields
        self.lot_processes_spinbox.delete(0, tk.END)
        self.lot_processes_spinbox.insert(0, "1")
        self.program_name_entry.delete(0, tk.END)
        self.execution_time_entry.delete(0, tk.END)
        self.execution_time_entry.insert(0, "00:00")
        self.program_number_entry.config(state="normal")
        self.program_number_entry.delete(0, tk.END)
        self.program_number_entry.config(state="readonly")
        self.operation_combobox.set("")
        for widget in self.operation_inputs_frame.winfo_children():
            widget.destroy()
