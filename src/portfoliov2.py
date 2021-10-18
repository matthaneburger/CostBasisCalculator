#!/usr/bin/env python3

#building out the skeleton for the program -- may look messy but will make code more modular as I get a better idea of how I want this structured
from yahoo_fin import stock_info as si
from aux_py.formatting import formatAsMoney as fm

class VanguardPortfolio():
    def __init__(self) -> None:
        pass

    def getLivePricesVanguardPortfolio(self):
        __cloudflare=si.get_live_price("NET")
        __apple=si.get_live_price("AAPL")
        __aehr=si.get_live_price("AEHR")
        __spacemobile=si.get_live_price("ASTS")
        __taiwansemiconductor=si.get_live_price("TSM")
        __denisonmines=si.get_live_price("DNN")
        __digitalturbine=si.get_live_price("APPS")
        __energyfuels=si.get_live_price("UUUU")
        settlementfund=16.95

        net=__cloudflare*10
        aapl=__apple*4
        aehr=__aehr*50
        asts=__spacemobile*300
        tsm=__taiwansemiconductor*6
        dnn=__denisonmines*250
        apps=__digitalturbine*100
        uuuu=__energyfuels*200

        total=net+aapl+aehr+asts+tsm+dnn+apps+uuuu+settlementfund

        print("Cloudflare: " + fm(net))
        print("Apple: " + fm(aapl))
        print("AEHR Test Systems: " + fm(aehr))
        print("ASTS Space Mobile: " + fm(asts))
        print("Taiwan Semiconductor: " + fm(tsm))
        print("Denison Mines: " + fm(dnn))
        print("Digital Turbine: " + fm(apps))
        print("Energy Fuels: " + fm(uuuu))

        print("Total: " + fm(total))

    

class CRSRLoss():
    def __init__(self) -> None:
        self.__costbasis=45.51
        self.__totalSharesOfCRSR=733
        self.__CRSRCurrentPrice=si.get_live_price("CRSR")
        print("crsr constructor")
    
    


def main():
    vp = VanguardPortfolio()
    crsr = CRSRLoss()
    vp.getLivePricesVanguardPortfolio()

if __name__ == "__main__":
    main()
