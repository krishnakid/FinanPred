#!/usr/bin/env python

import store
import load
from consts import *

import numpy			# Numerical Python Library
import csv				# Python CSV Library
import StringIO			# Read strings as Files
import datetime			# Python DateTime package

###### DEFINE constants ##########

# define a list of exchanges to follow
EXCHANGES = ["AMEX",	# American Stock Exchange
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

###### DEFINE utility functions ##########


# builds a start-stop tuple for the load functions
# 	st : a starting datetime
#	dur : a number of days to build the duration for
def buildInterval(st, dur):
	end = st + datetime.timedelta(days=dur)
	return (st, end)

###### EXECUTE main code ##########

#print load.loadData(STOCKS)
tstData = load.loadHisData(buildInterval(datetime.date.today() - 
									     datetime.timedelta(days=800), 500), STOCK)

tsFile = StringIO.StringIO(tstData)
# load into numpy-readable matrix.

store.storeHistData(tsFile, STOCK)				# test storage capabilities

#res = numpy.loadtxt(tsFile, delimiter=",", skiprows=0, usecols=(OPEN_CL,
#								HIGH_CL, LOW_CL, CLOSE_CL, VOLUME_CL))

# res now has a string containing a set of historical information.
# we may load this information into our mongo datastore.
#(rows, cols) = res.shape
#print "[{} x {}] entries found!".format(rows, cols)
print "================= TEST COMPLETE ==================="

# data vector loaded properly, now need to build neural net predictor.








