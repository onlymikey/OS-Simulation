from Services.lot_service import LotService

class LotController:
    def __init__(self):
        self.lot_service = LotService()

    def create_lot(self):
        """
        Crea un lote con los procesos pendientes.
        """
        msg = {
            'status': False,
            'type': 'Error',
            'message': ''
        }
        if self.lot_service.save_lot():
            msg['status'] = True
            msg['type'] = 'Success'
            msg['message'] = 'Lote creado exitosamente'
        else:
            msg['message'] = 'Error en el servicio de creación de Lotes'
        return msg