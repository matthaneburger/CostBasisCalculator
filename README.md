# Introduction
This small project is intended to help me keep track of my poor financial decision to invest in this company. :')

## More Info
Less succinctly, Vanguard does not have the ability to track your entire ROI for a singular asset class within an IRA. Essentially, the premiums you generate from selling covered calls on shares to offset paper losses won't calculate when viewing your performance history. This is just intended to show me that data. 

## To Run...
MacOS w/ Python Installed:

chmod +x ./driver.py

./driver.py

## Issues
Need to add error handling. Currently, the program fails with nasty looking TraceBack errors when the values on the numer of shares does not have a 1:1 value for share cost. 

## Next Steps
Main next steps is to put all of the data into a GetInfo() method and just make the getters and setters just return values. Originally, I was just making this program for the Ave. Cost Basis but then I started wanting more and more information. So, major refactoring is necessary.

Make program use ticker as input to draw data e.g. not make this CRSR-oriented. Potentially change input stream from Excel file to something different.

