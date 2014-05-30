==========================================================================
FinanPred : A Financial Predicion Suite                
==========================================================================

@author Rahul Dhodapkar (krishnakid)
@version 5.12.14

FinanPred is a financial prediction algorithm developed for fun by 
Rahul Dhodapkar (krishnakid) for the purpose of predicting stocks in the
hope that such a process could be automated and serve as a passive revenue
stream.

==========================================================================
Technologies Used 
==========================================================================

The base of the suite will be written in Python, making heavy use of the
numpy package.  Time allowing, certain core components may be rewritten
in C.

General Technologies:
	
	MongoDB:
		brew update
		brew install mongodb
			(start with)
			mongod --dbpath <path to data directory>

Python Packages:
	requests:
		pip install requests

	pymongo:
		pip install pymongo


==========================================================================
Points on Data Formatting 
==========================================================================

We will strive to adhere to a single standard representation of stock prices
during the development cycle. As the first major format encountered, the
majority of information will be passed in the Metastock data format
(Information on this format at the link below):

	http://www.stockhistoricaldata.com/historical-data-formats/metastock-data-format

==========================================================================
Data Sources and Input                                  
==========================================================================

######  Current Stock Information  #######################################

Data is currently pulled from the Yahoo Finance RESTful API, available 
through 

	http://finance.yahoo.com/d/quotes.csv

An unofficial set of documentation for this service is available at:

	http://www.gummy-stuff.org/Yahoo-data.htm

Unofficial documentation for the historical quote service is at:

	https://code.google.com/p/yahoo-finance-managed/wiki/csvHistQuotesDownload

######  Historical Stock Information  ####################################

Historical stock data is currently being pulled from

	http://finance.yahoo.com/q/hp?s=OXY
	http://ichart.finance.yahoo.com/table.csv?s=OXY&d=4&e=30&f=2014&g=d&a=11&b=31&c=1981&ignore=.csv

It seems as though a direct call to the ichart will be sufficient to extract
the information desired.  Information is returned in 

	Date,Open,High,Low,Close,Volume,Adj Close

Format 

==========================================================================
Data Cleaning and Missing Data                                 
==========================================================================

Since FinanPred is run on free, publically available financial data, it should
come as no surprise than our information is likely to be incomplete.  In 
order to account for missing information, data will be filled in with the last
open entry in the database at storage time.















