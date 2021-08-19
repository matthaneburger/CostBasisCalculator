#!/usr/bin/env python3
import sys
import os
from yahoo_fin import stock_info as si

class CRSROpportunityCost:
    __vtsax=si.get_live_price("vtsax")
    __numVTSAXshares=311.5150

    def __init__(self):
        pass

    def getVTSAX(self):
        return self.__vtsax
        
    def getInfo(self):
        print("Price of VTSAX: $" + str(round(self.getVTSAX(),2)))
