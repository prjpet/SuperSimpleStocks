# SuperSimpleStocks
A super simple stock trading software.

Assumptions:
- Stock price will not be 0, unless stock has not been traded before. Stock price can't be less than 0.

- Amount of stocks traded can't be 0 or less.
	
Documentation:
- The programmer has made every effort to produce easy to understand source code which also functions as documentation. Start with Main to understand program flow.
	
- Created using Python 3.4.3 (i.e.: requires the 3.4.3 interpreter at least)
	
Working mechanism (see example_run.png for more details):

AUTOMATIC INPUT (Main_Auto.py - added on 30/05/2016):
- The sole purpose of automatic functionality implementation is to prove that the calculations are correct

- The user now has the ability to create a list of trades in an Excel spreadsheet - same format as given in TradesSource.csv

- The excel spreadsheet can be used to verify calculations

- Only the first 5 columns are used - if they are in incorrect format, all errors SHOULD BE handled

- The first 4 columns are self-explaining: 
		- Stock Symbol (in case of error trade won't register in TradesManager and line will be excluded from counting)
		- Price (will be 1 in case of error)
		- Buy or Sell Indicator (in case of error trade won't register in TradesManager and line will be excluded from counting)
		- Quantity (will be 1 in case of error)
		
- The 5th column gives the ability to manipulate trade timestamp

- The number represents minutes (can only be integer format, can also be negative value - will be 0 in case of error)

- The first trade for each share has to be with a "0" timedelta to allow AllShareIndex calculations (if value higher than 14, will be made 0)

MANUAL INPUT (Main.py):
	
- Upon running the compiling the Main() block, the user is presented with the given information about the shares.
	
- The user chooses a share to trade, by entering the 3 letter stock symbol in the prompt (Any other input will trigger an error message, not case sensitive).
	
- The user then inputs the current market price of the stock (Any other input than numbers higher than 0 and dot separated will trigger an error message).
	
- Submitting a current market price triggers an immediate calculation and display of:
	- Dividend Yield
	- P/E Ratio
	
- The user then needs to input a trade which needs to be either "BUY" or "SELL" type (Any other input will trigger an error message, not case sensitive). 
	
- The user then is requested to input the amount of shares been traded (Has to be a whole number value, no decimals. any other input will trigger an error message).
	
- Submitting the trade type and traded amount will trigger an immediate registration of trade and display of all trades.
	
- The VWSP is calculated for all traded shares for the trades of the past 15 minutes and displayed after displaying the trades for the respective share. 
	
- GBCE All Share Index are calculated and displayed based on current market price of already traded shares.
