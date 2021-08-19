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
    
    def printWhatItWouldBeToday(self):
        print("What it would be today (Live Price): " + str(self.formatAsMoney(self.whatItWouldBeToday())))

    def formatAsMoney(self,number):
            return "${:,.2f}".format(number)
            
    def getInfo(self):
        print("Current price of VTSAX: " + str(self.formatAsMoney(self.getVTSAXPrice())))
        print("Value of Original Investment upon selling: " + str(self.formatAsMoney(self.priceOfOriginalInvestment())))
        print()