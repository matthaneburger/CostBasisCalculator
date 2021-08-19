# Introduction
This small project is intended to help me keep track of my poor financial decision to invest in this company. :')

## More Info
Less succinctly, Vanguard does not have the ability to track your entire ROI for a singular asset class within an IRA. Essentially, the premiums you generate from selling covered calls on shares to offset paper losses won't calculate when viewing your performance history. This is just intended to show me that data. 

## To Run...
MacOS w/ Python Installed:

chmod +x ./driver.py

./driver.py

##Output
![Alt text](/CostBasisCalculator/blob/master/src/assets/screenshotOutput.png?raw=true "Output")

## Issues
Need to add error handling. Currently, the program fails with nasty looking TraceBack errors when the values on the numberOfShares column don't have a 1:1 value for share cost. 

## Next Steps
Fixed Getters and Setters. Added GetInfo for CoveredCalls and CostBasis Classes. [FIXED]

Make program use ticker as input to draw data e.g. not make this CRSR-oriented. Potentially change input stream from Excel file to something different. [BACKLOG]

Create a GUI representing the opportunity cost of selling VTSAX to invest into this asset, as well as the price of Ave. Cost Basis needed to recoup losses. [INPROGRESS]

