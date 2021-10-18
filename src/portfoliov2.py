#!/usr/bin/env python3

#building out the skeleton for the program -- may look messy but will make code more modular as I get a better idea of how I want this structured
from yahoo_fin import stock_info as si
from aux_py.formatting import formatAsMoney as fm
# TODO: breaking imports into different classes once structured is settled

class VanguardPortfolio():
    def __init__(self) -> None:
        pass

    def opportunityCost(self):
        # TODO: add in VTSAX to track "Goal Number"
        # TODO: decide whether to import code from csrs_data
        pass

    def getLivePricesVanguardPortfolio(self):
        # TODO: will be fixing a lot of these hardcoded values later on
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

        # TODO: create print method -- this looks ugly
        print("Cloudflare: " + fm(net))
        print("Apple: " + fm(aapl))
        print("AEHR Test Systems: " + fm(aehr))
        print("ASTS Space Mobile: " + fm(asts))
        print("Taiwan Semiconductor: " + fm(tsm))
        print("Denison Mines: " + fm(dnn))
        print("Digital Turbine: " + fm(apps))
        print("Energy Fuels: " + fm(uuuu))

        print("Total: " + fm(total))

    
#for now, this is a class -- since it's static, can figure out if this is not necessary
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
