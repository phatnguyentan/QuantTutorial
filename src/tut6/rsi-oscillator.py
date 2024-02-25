import pandas_ta as ta
import pandas as pd

from backtesting import Backtest
from backtesting import Strategy
from backtesting.lib import crossover
from backtesting.test import GOOG

from multiprocessing import Pool
import os

class RsiOscillator(Strategy):

    upper_bound = 70
    lower_bound = 30
    rsi_window = 14

    # Do as much initial computation as possible
    def init(self):
        self.rsi = self.I(ta.rsi, pd.Series(self.data.Close), self.rsi_window)

    # Step through bars one by one
    # Note that multiple buys are a thing here
    def next(self):
        if crossover(self.rsi, self.upper_bound):
            self.position.close()
        elif crossover(self.lower_bound, self.rsi):
            self.buy()

def do_backtest(filename):
    print(filename)
    data = pd.read_csv(
        f"{os.path.join(os.path.dirname(__file__), 'data', filename)}",
        names=[
            "OpenTime",
            "Open",
            "High",
            "Low",
            "Close",
            "Volume",
            "CloseTime",
            "QuoteVolume",
            "NumTrades",
            "TakerBuyBaseVol",
            "TakerBuyQuoteVol",
            "Unused"
        ]
    )
    data["OpenTime"] = pd.to_datetime(data["OpenTime"], unit="ms")
    data.set_index("OpenTime", inplace=True)

    bt = Backtest(GOOG, RsiOscillator, cash=10_000_000, commission=.002)
    stats = bt.run()
    sym = filename.split("-")[0]
    return (sym, stats["Return [%]"])

if __name__ == "__main__":
    data_path = os.path.join(os.path.dirname(__file__), "data")
    with Pool() as p:
        results = p.map(do_backtest, os.listdir(data_path))
    print(results)
