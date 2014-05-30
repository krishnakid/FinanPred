#!/usr/bin/env python

import requests				# HTTP request library
import json					# Python JSON library
import cookielib			# Python library for cookies
import datetime				# Python datetime library

########   load.py   ##################
#
# A simple toy script to load financial data in from Yahoo.  In the
# completed suite, this script will load from multiple sources and
# aggregate them into a single standardized format for analysis.

####### define CONSTANTS ##############

curURL = "http://finance.yahoo.com/d/quotes.csv"

hisURL = "http://ichart.finance.yahoo.com/table.csv"

####### define METHODS   ##############

# load current stock data
# 	syms : a list of symbols to get data for
def loadCurData(syms):
	data = {
		"s" : "+".join(syms),
		"f" : "snd1l1yr"
	}
	r = requests.get(curURL, params=data)
	return r.text

# load historical stock data
# 	bnd : range of datetime objects to obtain data from
#	sym : a symbol to get data for
def loadHisData(bnd, sym): 
	(fr, to) = bnd
	((frm, frd, fry), (tom, tod, toy)) = ((fr.month, fr.day, fr.year),
										  (to.month, to.day, to.year))
	print "========= LOADING {} ============" .format(sym)
	data = {
		"s" : sym,
		"a" : frm - 1,
		"b" : frd,
		"c" : fry,
		"d" : tom - 1,
		"e" : tod,
		"f" : toy,
		"g" : "d",
		"ignore" : ".csv"
	}
	r = requests.get(hisURL, params=data)
	retText = "\n".join(r.text.split("\n")[1:])		# naive header strip.
	return retText


