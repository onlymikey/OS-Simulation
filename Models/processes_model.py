class Process:
    def __init__(self,
                 program_name: str,
                 execution_time: str,
                 program_number: str,
                 operation: str,
                 input1: float,
                 input2: float,
                 status: str = "En Cola"):
        self.program_name = program_name
        self.execution_time = execution_time
        self.program_number = program_number
        self.operation = operation
        self.input1 = input1
        self.input2 = input2
        self.status = status