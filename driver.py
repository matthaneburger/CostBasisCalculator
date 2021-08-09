#!/usr/bin/env python3
from costBasis import CRSRCostBasis
import sys
import os
import pandas as pd
import costBasis
from coveredCalls import CRSRCoveredCallsTracker
from yahoo_fin import stock_info as si

#retrieval of excel data frames
crsr_shares_df = pd.read_excel('./CRSRTrackingGrid.xlsx',
                                        dtype={"NumberOfShares":int,
                                                "CostPerShare":float},
                                        sheet_name="CRSRShares")
crsr_ccs_df = pd.read_excel('./CRSRTrackingGrid.xlsx',
                                        dtype={"ccPremiumGained ":float,
                                                "ccPremiumPaid ":float},
                                        sheet_name="CRSRCoveredCalls")

#objects created from outside classes
crsrCostBasis = CRSRCostBasis()
crsrCCs = CRSRCoveredCallsTracker()

#retrieves all values from excel sheet
shares_numberOfShares = crsr_shares_df['NumberOfShares'].values
shares_costPerShare = crsr_shares_df['CostPerShare'].values
options_premiumGained = crsr_ccs_df['ccPremiumGained'].values
options_premiumPaid = crsr_ccs_df['ccPremiumPaid'].values

#updates cost basis when every transaction is processed
for i in range(shares_costPerShare.size):
    crsrCostBasis.transaction(shares_numberOfShares[i],shares_costPerShare[i])

#iterations add all the premium gained minus the premium paid for covered calls
for i in range(options_premiumGained.size):
    crsrCCs.sellCoveredCall(options_premiumGained[i])
for i in range(options_premiumPaid.size):
    crsrCCs.purchasedCoveredCall(options_premiumPaid[i])

#methods to display data
crsrCostBasis.getNumberOfShares()
crsrCostBasis.totalCostBasis()
crsrCCs.getCCInfo()
crsr_price=si.get_live_price("crsr")
print("Current Price: $" + str(round(crsr_price,2)))