# SuperSimpleStocks
A super simple stock trading software.

Assumptions:
1. Stock price will not be 0, unless stock has not been traded before. Stock price can't be less than 0.

2. Amount of stocks traded can't be 0 or less.
	
Documentation:
- The programmer has made every effort to produce easy to understand source code which also functions as documentation. Start with Main to understand program flow.
	
- Created using Python 3.4.3 (i.e.: requires the 3.4.3 interpreter at least)
	
Working mechanism (see example_run.png for more details):
- The software is operated manually - thanks to the modular design, automated functionality is easy to implement but not a requirement.
	
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
