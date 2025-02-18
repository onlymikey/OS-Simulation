class Lot:
    def __init__(self, lot_id: int, processes: list):
        """
        Representa un lote que contiene múltiples procesos.

        :param lot_id: Identificador único del lote.
        :param processes: Lista de objetos de tipo Process.
        """
        self.lot_id = lot_id
        self.processes = processes