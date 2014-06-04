#!/usr/bin/env python

from consts import *		# load constants header

import pymongo				# Python mongo driver
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

histURL = "http://ichart.finance.yahoo.com/table.csv"


######## DEFINE globals ################

client = None				# global client, for connection efficiency
							# during read/write cycles

db = None					# database

######## DEFINE utilities ##############

# open global client connection
def openClient():
	global client, db 		# prevent variable shadowing
	client = pymongo.MongoClient()
	db = client.test_db
	print "load.py :: client successfully created"

# close global client connection
def closeClient():
	global client, db 		# prevent variable shadowing
	client.disconnect()
	client = db = None
	print "load.py :: client successfully destroyed"

####### define METHODS   ##############

# load current stock data
# 	syms : a list of symbols to get data for
def loadExtCurData(syms):
	data = {
		"s" : "+".join(syms),
		"f" : "snd1l1yr"
	}
	r = requests.get(curURL, params=data)
	return r.text

# load historical stock data from local mongod instance
#	bnd : range of datetime objects to obtain data from
#	sym : a symbol to get data for
def loadHistData(bnd, sym):
	openClient()
	(fr, to) = bnd
	res = db[MDB_HIST_COLLECTION].find({"date" : {"$gte" : fr, "$lte" : to} }, 
									   {"close" : 1, "_id" : 0})

	for vals in res:
		print vals


	closeClient()

# load historical stock data from Yahoo
# 	bnd : range of datetime objects to obtain data from
#	sym : a symbol to get data for
def loadExtHistData(bnd, sym): 
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
	r = requests.get(histURL, params=data)
	retText = "\n".join(r.text.split("\n")[1:])		# naive header strip.
	return retText


