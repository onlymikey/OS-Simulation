import re
from Services.processes_service import ProcessesService

class ProcessController:
    def __init__(self):
        self.processes_service = ProcessesService()

    @staticmethod
    def validate_process_data(lot_processes, program_name, execution_time, program_number, operation, input1=None, input2=None) -> dict:
        """Valida los datos de los procesos"""
        msg = {
            'status': False,
            'type': 'Error',
            'message': ''
        }

        # 1. Validar que los campos obligatorios no estén vacíos
        if not lot_processes or not program_name or not execution_time or not program_number or not operation:
            msg['message'] = 'Todos los campos son obligatorios'
            return msg

        # 2. Validar que lot_processes sea un número entero positivo
        if not lot_processes.isdigit() or int(lot_processes) <= 0:
            msg['message'] = 'El número de procesos por lote debe ser un número entero positivo'
            return msg

        # 3. Validar el formato de execution_time (mm:ss)
        if not re.match(r'^\d{2}:\d{2}$', execution_time):
            msg['message'] = 'El tiempo de ejecución debe estar en formato mm:ss'
            return msg
        minutes, seconds = execution_time.split(":")
        try:
            minutes = int(minutes)
            seconds = int(seconds)
            if not (0 <= minutes < 60) or not (0 <= seconds < 60):
                msg['message'] = 'Los minutos y los segundos deben estar en el rango de 00:00 a 59:59'
                return msg
            if minutes == 0 and seconds == 0:
                msg['message'] = 'El tiempo de ejecución debe ser mayor a 0 segundos'
                return msg
        except ValueError:
            msg['message'] = 'El tiempo de ejecución debe ser un número entero en formato mm:ss'
            return msg


    # 4. Validar la operación seleccionada
        if not operation:
            msg['message'] = 'Debe seleccionar una operación'
            return msg

        # 5. Validar los datos dependiendo de la operación seeleccionada
        if operation == 'Suma' or operation == 'Resta' or operation == 'Multiplicación' or operation == 'División':
            # Validar que input1 e input2 sean números
            if not input1 or not input2:
                msg['message'] = 'Los campos de dato son obligatorios'
                return msg
            if not input1.isdigit() or not input2.isdigit():
                msg['message'] = 'Los campos de dato deben ser números enteros'
                return msg
            if operation == 'División' and int(input2) == 0:
                msg['message'] = 'No se puede dividir por cero'
                return msg

        # Si todos los datos son válidos
        msg['status'] = True
        msg['type'] = 'Success'
        msg['message'] = 'Proceso creado correctamente'
        return msg

    def create_process(self, lot_processes, program_name, execution_time, program_number, operation, input1, input2) -> dict:
        """Crea un proceso con los datos proporcionados"""
        # Validar los datos del proceso
        msg = self.validate_process_data(lot_processes, program_name, execution_time, program_number, operation, input1, input2)
        if not msg['status']:
            return msg
        if self.processes_service.create_process(program_name, execution_time, program_number, operation, input1, input2):
            msg['status'] = True
            msg['type'] = 'Success'
            msg['message'] = 'Proceso creado exitosamente'
        else:
            msg['message'] = 'Error en el servicio de creación de procesos'
        return msg
