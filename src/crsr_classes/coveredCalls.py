#!/usr/bin/env python3
import sys
import os

class CRSRCoveredCallsTracker:
    __runningTotal=0
    __coveredCallsPremium=0
    __coveredCallsCost=0
    def __init__(self):
        pass
    def sellCoveredCall(self,profit):
        self.__runningTotal+=profit
        self.__coveredCallsPremium+=profit
    def purchasedCoveredCall(self,cost):
        self.__runningTotal-=cost
        self.__coveredCallsCost+=cost
    def getTotalCCProfit(self):
        return self.__runningTotal
    def getCCCost(self):
        return self.__coveredCallsCost
    def getCCPremium(self):
        return self.__coveredCallsPremium
    def getInfo(self):
        print("Premium from selling CC's: $" + str(self.getCCPremium()))
        print("Cost of buying CC's: $" + str(self.getCCCost()))
        print("Total ROI from Covered Calls: $" + str(self.getTotalCCProfit()))