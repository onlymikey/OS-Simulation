from Models.processes_model import Process
# from Logic.processes_logic import ProcessesLogic

class ProcessesService:
        @staticmethod
        def create_buy(folio: str, user_id: int, iup_supplier: str, total: float, date: str) -> Optional[int]:
            buy = Buy(folio=folio, user_id=user_id, iup_supplier=iup_supplier, total=total, date=date)
            return BuyDAO.create_buy(buy)

