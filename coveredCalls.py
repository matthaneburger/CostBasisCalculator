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
        print("Total ROI from Covered Calls: $" + str(self.__runningTotal))
    def getCCCost(self):
        print("Cost of buying Covered Calls: $" + str(self.__coveredCallsCost))
    def getCCPremium(self):
        print("Premium from selling Covered Calls: $" + str(self.__coveredCallsPremium))
