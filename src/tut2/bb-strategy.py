from backtesting import Backtest, Strategy
from backtesting.test import GOOG
import numpy as np
import pandas_ta as ta

def indicator(data):
    # data is going to be our OHLCV
    bbands = ta.bbands(close = data.Close.s, std = 1)
    print(bbands)
    return bbands
    # return bbands.to_numpy().T[:3]

print(GOOG)
class BBStrategy(Strategy):
    
    def init(self):
        self.bbands = self.I(indicator, self.data)
        pass
    def next(self):
        lower_band = self.bbands[0]
        upper_bank = self.bbands[2]
        if self.position:
            if self.data.Close[-1] > upper_bank[-1]:
                self.position.close()
        else:
            if self.data.Close[-1] < lower_band[-1]:
                self.buy()


bt = Backtest(GOOG, BBStrategy, cash=10_000)
stats = bt.run()
bt.plot()
print(stats)