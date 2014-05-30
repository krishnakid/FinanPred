#!/usr/bin/env python

import store
import load
from consts import *

import numpy			# Numerical Python Library
import csv				# Python CSV Library
import StringIO			# Read strings as Files



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
tstData = load.loadHisData( ((3, 14, 2010),(8, 14, 2010)), STOCK)

tsFile = StringIO.StringIO(tstData)
# load into numpy-readable matrix.
res = numpy.loadtxt(tsFile,delimiter=",",skiprows=1,usecols=(OPEN_CL,
								HIGH_CL, LOW_CL, CLOSE_CL, VOLUME_CL))
print res

# data vector loaded properly, now need to build neural net predictor.








