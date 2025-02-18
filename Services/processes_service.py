from Models.lot_model import Lot
from Models.processes_model import Process
from Services.lot_service import LotService

class ProcessesService:
    @staticmethod
    def create_process(program_name: str, execution_time: str, program_number: str, operation: str,
                       input1: float, input2: float, status: str = "En Cola") -> Lot:
        """
        Encapsula los parámetros en un objeto Process.
        """
        process = Process(
            program_name=program_name,
            execution_time=execution_time,
            program_number=program_number,
            operation=operation,
            input1=input1,
            input2=input2,
            status=status
        )
        return LotService.add_process_to_lot(process)