class Martingale():
    def __init__(self, invest_def=1, percent=1.27, maxMatingale=100):
        self.percent = percent
        self.max_martingale = maxMatingale
        self.invest_def = invest_def

        self.invest_current = self.invest_def

    def getCurrentInvest(self):
        return self.invest_current

    def calc(self, result):
        if result == 'loose':
            self.invest_current = self.invest_current * 2 * self.percent
            if self.invest_current > self.max_martingale:
                return round(self.invest_def, 2)
            return round(self.invest_current, 2)
        else:
            self.invest_current = self.invest_def
            return round(self.invest_def, 2)


if __name__ == "__main__":
    pass