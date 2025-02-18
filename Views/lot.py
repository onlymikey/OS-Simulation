import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import time
import uuid


class BatchUI:
    def __init__(self, master):
        self.master = master

        # Timer for global execution time
        self.global_timer = 0
        self.running = False

        # Set up grid layout
        self.master.columnconfigure(0, weight=1)
        self.master.columnconfigure(1, weight=2)
        self.master.rowconfigure(0, weight=1)

        # Treeview for batches and processes
        self.tree = ttk.Treeview(self.master)
        self.tree.grid(row=0, column=0, sticky="nswe", padx=(10, 0), pady=10)

        # Add scrollbar for the treeview
        self.tree_scroll = ttk.Scrollbar(self.master, orient="vertical", command=self.tree.yview)
        self.tree_scroll.grid(row=0, column=1, sticky="ns", pady=10)
        self.tree.configure(yscrollcommand=self.tree_scroll.set)

        # Configure columns in the Treeview
        self.tree.heading("#0", text="Lotes y Procesos", anchor="w")
        self.tree.bind("<<TreeviewSelect>>", self.display_details)

        # Frame for details on the right
        self.details_frame = ttk.Frame(self.master)
        self.details_frame.grid(row=0, column=1, sticky="nswe", padx=10, pady=10)

        # Add widgets for batch/process details
        self.details_label = ttk.Label(self.details_frame, text="Detalles", font=("Arial", 16))
        self.details_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.info_label_1 = ttk.Label(self.details_frame, text="")
        self.info_label_1.grid(row=1, column=0, columnspan=2, pady=5)

        self.info_label_2 = ttk.Label(self.details_frame, text="")
        self.info_label_2.grid(row=2, column=0, columnspan=2, pady=5)

        # Global timer label
        self.global_timer_label = ttk.Label(self.details_frame, text="Tiempo total de ejecución: 0s", font=("Arial", 14))
        self.global_timer_label.grid(row=3, column=0, columnspan=2, pady=(20, 10))

        # Populate the Treeview with example data
        self.populate_tree()

        # Start global timer
        self.start_timer()

    def populate_tree(self):
        # Add sample batches and processes
        for i in range(3):  # 3 batches
            batch_id = f"Lote {i+1}"
            batch_node = self.tree.insert("", "end", text=batch_id, open=True)
            for j in range(4):  # 4 processes per batch
                process_id = f"Proceso {j+1}"
                self.tree.insert(batch_node, "end", text=process_id)

    def display_details(self, event):
        # Get selected item
        selected_item = self.tree.selection()[0]
        item_text = self.tree.item(selected_item, "text")

        # Check if it's a batch or a process
        if "Lote" in item_text:  # It's a batch
            self.info_label_1.config(text=f"Número de programa: {uuid.uuid4().hex[:8]}")
            self.info_label_2.config(text="Tiempo estimado de ejecución: 10:00")
        elif "Proceso" in item_text:  # It's a process
            self.info_label_1.config(text="Nombre del programador: Usuario")
            self.info_label_2.config(text="Operación: A + B = C\nTiempo ejecutado: 5s\nTiempo restante: 5s")

    def start_timer(self):
        # Start global timer
        self.running = True
        self.update_timer()

    def update_timer(self):
        if self.running:
            self.global_timer += 1
            self.global_timer_label.config(text=f"Tiempo total de ejecución: {self.global_timer}s")
            self.master.after(1000, self.update_timer)

    def stop_timer(self):
        # Stop global timer
        self.running = False
