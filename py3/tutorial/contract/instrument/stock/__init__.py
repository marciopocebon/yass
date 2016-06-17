from .... import contract


class Stock(contract.Instrument):
    def __init__(self):
        super().__init__()
        self.paysDividend = None  # type: bool
