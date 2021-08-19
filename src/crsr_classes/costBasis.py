#!/usr/bin/env python3
from aux_py.colors import bcolors
from aux_py.formatting import formatAsMoney as fm
from yahoo_fin import stock_info as si

class CRSRCostBasis:
    __sumOfCostBasis=0
    __totalNumberOfShares=0
    __crsr_price=si.get_live_price("CRSR")

    def __init__ (self):
        pass

    def transaction(self,numberOfShares,price):
        self.numberOfShares = numberOfShares
        self.price = price
        self.__totalNumberOfShares+=numberOfShares
        self.costBasis=numberOfShares*price
        self.__sumOfCostBasis+=self.costBasis
        return self.costBasis

    def totalCostBasis(self):
        result=self.__sumOfCostBasis/self.__totalNumberOfShares
        return result
    
    def getCurrentPrice(self):
        return self.__crsr_price

    def getNumberOfShares(self):
        return self.__totalNumberOfShares

    def calculateProfitLossPercentage(self):
        self.currentValue=self.__totalNumberOfShares*self.__crsr_price
        self.gainloss=(self.currentValue-self.__sumOfCostBasis)/self.__sumOfCostBasis
        if(self.gainloss>0):
            return bcolors.OKGREEN + str('{:.3%}'.format(self.gainloss)) + bcolors.ENDC
        elif(self.gainloss<0):
            return bcolors.FAIL + str('{:.3%}'.format(self.gainloss)) + bcolors.ENDC
    
    def calculatePaperGainLoss(self):
        self.currentValue=self.__totalNumberOfShares*self.__crsr_price
        self.gainloss=(self.currentValue-self.__sumOfCostBasis)
        if(self.gainloss>0):
            return bcolors.OKGREEN +"$"+str(fm(abs(self.gainloss)))+bcolors.ENDC
        elif(self.gainloss<0):
            return bcolors.FAIL +"-"+str(fm(abs(self.gainloss)))+bcolors.ENDC
    
    def valueOfCurrentInvestment(self):
        return self.__totalNumberOfShares * self.__crsr_price
    
    def printCurrentInvestmentValue(self):
        print("Current Value of CRSR Investment: " + str(fm(self.valueOfCurrentInvestment())))

    def getInfo(self):
        print("Total Shares of CRSR: " +str(self.getNumberOfShares()))
        print("Running Ave. Cost Basis: " + str(fm(self.totalCostBasis())))
        print("Current Price CRSR: " + str(fm(self.getCurrentPrice())))
        print("Percentage Gain/Loss: " + self.calculateProfitLossPercentage())
        print("Total Paper Gain/Loss: " + self.calculatePaperGainLoss())
        print()