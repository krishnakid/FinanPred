#!/usr/bin/env python

import store
import load

###### DEFINE constants ##########

# define a list of exchanges to follow
EXCHANGES = ["AMEX",		# American Stock Exchange
		  "AMS",		# Euronext Amsterdam
		  "BRU",		# Euronext Brussels
		  "CBOT",		# Chicago Board of Trade
		  "CFE",		# Chicago Futures Exchange
		  "CME",		# Chicago Mercantile Exchange
		  "COMEX",		# New York Commodity Exchange
		  "NASDAQ",		# NASDAQ Stock Exchange
		  "LSE",		# London Stock Exchange
		  "SGX"			# Singapore Stock Exchange
		  ]

STOCKS = ["CMG",
		  "JNJ",
		  "MSFT"
		 ]

# single stock for testing purposes.
STOCK = ["OXY"]

#print load.loadData(STOCKS)
print load.loadHisData( ((3, 14, 2010),(8, 14, 2010)), STOCKS)

