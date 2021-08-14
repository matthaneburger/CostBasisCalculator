#!/usr/bin/env python3
import sys
import os
from aux_py.colors import bcolors
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
        #TODO: return the overall paper gain or loss
        self.currentValue=self.__totalNumberOfShares*self.__crsr_price
        self.gainloss=(self.currentValue-self.__sumOfCostBasis)
        if(self.gainloss>0):
            return bcolors.OKGREEN +"$"+str(round(abs(self.gainloss),2))+bcolors.ENDC
        elif(self.gainloss<0):
            return bcolors.FAIL +"-$"+str(round(abs(self.gainloss),2))+bcolors.ENDC

    def getInfo(self):
        print("Total Shares of CRSR: " +str(self.getNumberOfShares()))
        print("Running Ave. Cost Basis: $" + str(round(self.totalCostBasis(),2)))
        print("Current Price CRSR: $" + str(round(self.getCurrentPrice(),2)))
        print()
        print("Percentage Gain/Loss: " + self.calculateProfitLossPercentage())
        print("Total Paper Gain/Loss: " + self.calculatePaperGainLoss())
        print()