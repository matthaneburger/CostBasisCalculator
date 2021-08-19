#!/usr/bin/env python3
import requests as rq
import yfinance as yf

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

    def getInfo(self):
        print("Current price of VTSAX: $" + str(round(self.getVTSAXPrice(),2)))
        print("Value of Original Investment upon selling: $" + str(round(self.priceOfOriginalInvestment(),2)))
        print("What it would be today (Live Price): $" + str(round(self.whatItWouldBeToday(),2)))