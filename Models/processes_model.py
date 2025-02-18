class Process:
    def __init__(self,
                 program_name: str,
                 execution_time: str,
                 program_number: str,
                 operation: str,
                 input1: float,
                 input2: float,
                 status: str = "En Cola"):
        """
        Modelo de proceso.

        :param program_name: Nombre del programa.
        :param execution_time: Tiempo estimado de ejecución.
        :param program_number: Número único del programa (UUID).
        :param operation: Operación que realizará el programa (Suma, Resta, etc.).
        :param input1: Primer dato de la operación.
        :param input2: Segundo dato de la operación.
        :param status: Estado del proceso ('En Cola', 'En Ejecución', 'Completado', 'Error').
        """
        self.program_name = program_name
        self.execution_time = execution_time
        self.program_number = program_number
        self.operation = operation
        self.input1 = input1
        self.input2 = input2
        self.status = status