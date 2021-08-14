#!/usr/bin/env python3
import sys
import os
import pandas as pd
from crsr_classes.costBasis import CRSRCostBasis
from crsr_classes.coveredCalls import CRSRCoveredCallsTracker

#retrieval of excel data frames
crsr_shares_df = pd.read_excel('./crsr_data/CRSRTrackingGrid.xlsx',
                                        dtype={"NumberOfShares":int,
                                                "CostPerShare":float},
                                        sheet_name="CRSRShares")
crsr_ccs_df = pd.read_excel('./crsr_data/CRSRTrackingGrid.xlsx',
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
crsrCostBasis.getInfo()
crsrCostBasis.totalCostBasis()
crsrCCs.getInfo()