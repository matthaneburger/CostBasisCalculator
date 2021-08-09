#!/usr/bin/env python3
import sys
import os

class CRSRCostBasis:
    __sumOfCostBasis=0
    __totalNumberOfShares=0
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
    def getNumberOfShares(self):
        return self.__totalNumberOfShares
    def getInfo(self):
        print("Total Shares of CRSR: " +str(self.getNumberOfShares()))
        print("Running Cost Basis: " + str(round(self.totalCostBasis(),2)))