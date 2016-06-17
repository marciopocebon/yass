from typing import Any

from . import contract as c
from .contract import instrument as ci
from .contract.instrument import stock as cis

bond = ci.Bond()  # type: ci.Bond
bond.id = c.Integer(123)
bond.name = "ABB"
bond.coupon = 1.5
bond.expiration = c.Expiration("21.07.2016")
# bond.blabla = 123
# bond.name = 123
print("bond:", vars(bond))

stock = cis.Stock()  # type: cis.Stock
stock.id = c.Integer(123)
stock.name = "ABB"
stock.paysDividend = True
print("stock:", vars(stock))

try:
    uie = c.UnknownInstrumentsException()  # type: c.UnknownInstrumentsException
    uie.instrumentIds = [c.Integer(333), c.Integer(444)]
    uie.onlyNeededForTests2 = b'abc'
    raise uie
except c.UnknownInstrumentsException as e:
    print("exception:", e.instrumentIds, e.onlyNeededForTests2)

print(c.PriceKind.ASK)


class EchoServiceImpl(c.EchoService):
    def __init__(self):
        super().__init__()

    def echo(self, value: Any) -> Any:
        return value


echoService = EchoServiceImpl()  # type: c.EchoService
print(echoService.echo("Hello World!"))

node1 = c.Node()  # type: c.Node
node1.id = 1111111111111111111111111111111111111
node2 = c.Node()  # type: c.Node
node2.id = 2222222222222222222222222222222222222
node2.links = [node1, node2]
