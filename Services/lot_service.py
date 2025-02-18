from Models.lot_model import Lot
from Models.processes_model import Process

class LotService:
    # Lista temporal para acumular procesos
    pending_processes = []
    # Lista de lotes creados
    lots = []

    @staticmethod
    def add_process_to_lot(process: Process):
        """
        Añade un proceso a la lista temporal de procesos pendientes.
        """
        LotService.pending_processes.append(process)
        # DEBUG
        print(f"Proceso añadido al lote temporal: {process}")
        print(f"Procesos acumulados actualmente: {len(LotService.pending_processes)}")

    @staticmethod
    def save_lot():
        """
        Crea y guarda un nuevo lote con los procesos pendientes actuales.
        """
        if not LotService.pending_processes:
            print("No hay procesos pendientes para crear un lote.")
            return None  # No se puede crear un lote sin procesos

        # Generar un nuevo ID para el lote
        lot_id = len(LotService.lots) + 1
        # Crear un nuevo lote con los procesos acumulados
        lot = Lot(lot_id, processes=LotService.pending_processes.copy())
        # Vaciar la lista temporal
        LotService.pending_processes.clear()
        # Guardar el lote en la lista global de lotes
        LotService.lots.append(lot)
        print(f"Lote creado y guardado: {lot}")
        return lot
