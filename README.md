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
Data Sources and Input                                  
==========================================================================

Data is currently pulled from the Yahoo Finance RESTful API, available 
through 

	http://finance.yahoo.com/d/quotes.csv

An unofficial set of documentation for this service is available at:

	http://www.gummy-stuff.org/Yahoo-data.htm

Unofficial documentation for the historical quote service is at:

	https://code.google.com/p/yahoo-finance-managed/wiki/csvHistQuotesDownload
	

