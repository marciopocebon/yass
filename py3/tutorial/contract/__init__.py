from enum import Enum
from typing import List, Any


# todo: abstract
class ApplicationException(Exception):
    def __init__(self):
        pass


class EchoService:
    def echo(self, value: Any) -> Any:
        raise NotImplementedError()


# todo: model internal base type
class Expiration:
    def __init__(self, value: str) -> None:
        self.value = value  # type: str

    def __repr__(self) -> str:
        return self.value


# todo: model external base type; this is a wrapper for a Java Integer
class Integer:
    def __init__(self, value: int) -> None:
        self.value = value  # type: int

    def __repr__(self) -> str:
        return str(self.value)


# todo: abstract
class Instrument:
    def __init__(self):
        self.id = None  # type: 'Integer'
        self.name = None  # type: str


class Node:
    def __init__(self):
        self.id = None  # type: int
        self.links = None  # type: List['Node']


class Price:
    def __init__(self):
        self.instrumentId = None  # type: 'Integer'
        self.value = None  # type: 'Integer'
        self.kind = None  # type: 'PriceKind'


class PriceEngine:
    def subscribe(self, instrumentIds: List['Integer']) -> None:
        raise NotImplementedError()


class PriceKind(Enum):
    BID = 0
    ASK = 1


class PriceListener:
    def newPrices(self, prices: List['Price']) -> None:
        raise NotImplementedError()


class SystemException(Exception):
    def __init__(self):
        self.message = None  # type: str


class UnknownInstrumentsException(ApplicationException):
    def __init__(self):
        super().__init__()
        self.instrumentIds = None  # type: List['Integer']
        self.onlyNeededForTests1 = None  # type: any
        self.onlyNeededForTests2 = None  # type: bytes
