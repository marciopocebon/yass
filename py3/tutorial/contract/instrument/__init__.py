from typing import List

from ... import contract


class Bond(contract.Instrument):
    def __init__(self):
        super().__init__()
        self.coupon = None  # type: float
        self.expiration = None  # type: 'contract.Expiration'


class InstrumentService:
    def getInstruments(self) -> List['contract.Instrument']:
        raise NotImplementedError()

    def showOneWay(self, testBoolean: bool, testInt: int) -> None:
        raise NotImplementedError()
