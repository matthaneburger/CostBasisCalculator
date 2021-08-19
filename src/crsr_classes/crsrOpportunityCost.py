#!/usr/bin/env python3
import yfinance as yf
from aux_py.formatting import formatAsMoney as fm

class CRSROpportunityCost:
    __numVTSAXshares=311.5150
    __priceVTSAXSold=100.24
    __data=yf.download('VTSAX')

    def getVTSAXPrice(self):
        price=self.__data['Close'][-1]
        return price

    def priceOfOriginalInvestment(self):
        return self.__numVTSAXshares*self.__priceVTSAXSold
    
    def whatItWouldBeToday(self):
        return self.__numVTSAXshares*self.getVTSAXPrice()
    
    def printWhatItWouldBeToday(self):
        print("What it would be today (Live Price): " + str(fm(self.whatItWouldBeToday())))
            
    def getInfo(self):
        print("Current price of VTSAX: " + str(fm(self.getVTSAXPrice())))
        print("Value of Original Investment upon selling: " + str(fm(self.priceOfOriginalInvestment())))
        print()