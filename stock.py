class Stock():
    """Represent a simple stock profile."""

    def __init__(self, Symbol, Date, Close):
        """Initialize the stock"""
        self.self = self
        self.Symbol = Symbol
        self.Date = Date
        self.Close = Close
        self.stockClose = []
        self.dayStockClosed = []
     

		
    def addClose(self, stock, date):
        """Add information to the class"""
        self.stockClose.append(stock)
        self.dayStockClosed.append(date)
        




