#!/usr/bin/env python3

#building out the skeleton for the program -- may look messy but will make code more modular as I get a better idea of how I want this structured
import os
from Pre_CRSR.crsr_classes.costBasis import CRSRCostBasis
from yahoo_fin import stock_info as si
from Pre_CRSR.aux_py.colors import bcolors
from Pre_CRSR.aux_py.formatting import formatAsMoney as fm
import yfinance as yf

# TODO: breaking imports into different classes once structured is settled

class VanguardPortfolio:
    # TODO: find convention for global variables
    __totalEquity=0

    def __init__(self) -> None:
        pass
        
    def opportunityCost(self):
        # TODO: add in VTSAX to track "Goal Number"
        # TODO: decide whether to import code from csrs_data
        pass

        # TODO: create methods to separate out this logic. for now, writing it in the validate method
    def validator(self, ticker, costbasis, numbershares):
        try:
            price=si.get_live_price(ticker)
            number=fm(numbershares*costbasis)
            print("Your equity in {} is {}".format(ticker,number))
        except AssertionError:
            print(bcolors.FAIL + ticker + " does not exist.")
    
    def validateTicker(self, ticker):
        tickerFlag=yf.Ticker(ticker)
        info=None
        try:
            info = tickerFlag.info
        except:
            print(f"Cannot get info of {ticker}. Please check if it is valid.")
            exit()
            
    def addTransaction(self, ticker, costbasis, numbershares):
        livePrice = si.get_live_price(ticker)
        self.__totalEquity += costbasis*numbershares
    
    def printInfo(self):
        print("New Investment: " + str(fm(self.__totalEquity)))

#for now, this is a class -- since it's static, can figure out if this is not necessary
class CRSRLoss:

    def __init__(self) -> None:
        self.__costbasis=45.51
        self.__totalSharesOfCRSR=733
        self.__CRSRCurrentPrice=si.get_live_price("CRSR")
    
    def getCRSRInitialCost(self):
        return self.__costbasis*self.__totalSharesOfCRSR
    
    def getValueOfCurrentInvestment(self):
        return self.__totalSharesOfCRSR*self.__CRSRCurrentPrice
    
    def getCRSRLivePrice(self):
        return self.__CRSRCurrentPrice
    
    def printInfo(self):
        print(fm(self.getCRSRInitialCost()))
        print(fm(self.getValueOfCurrentInvestment()))

def main():

    vp = VanguardPortfolio()

    vp.addTransaction("NET",10,172.77)
    vp.addTransaction("AAPL",4,144.48)
    vp.addTransaction("ASTS",300,10.316)
    vp.addTransaction("TSM",6,114.07)
    vp.addTransaction("DNN",250,1.81)
    vp.addTransaction("UUUU",200,8.35)
    vp.addTransaction("APPS",100,87.35)
    vp.addTransaction("AEHR",50,21.47)

    vp.printInfo()
    #crsr = CRSRLoss()
    #vp.getLivePricesVanguardPortfolio()

if __name__ == "__main__":
    main()
