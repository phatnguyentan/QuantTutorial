from backtesting import Backtest
from backtesting.test import GOOG
from backtesting.lib import TrailingStrategy

class Strat(TrailingStrategy):

    def init(self):
        super().init()
        super().set_trailing_sl(1)

    # Step through bars one by one
    def next(self):
        super().next()
        price = self.data.Close[-1]

        if self.position:
            pass
        else:
            # Look at _Broker class for details on order processing
            # What happens when we have sl and tp, etc.
            self.buy(size=1, sl=price - 5, tp=price + 10)

# might want trade_on_close = True to deal with gapping for sl and tp
bt = Backtest(GOOG, Strat, cash=10_000)
bt.run()

bt.plot()
