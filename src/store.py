#!/usr/bin/env python

from consts import *		# local constants header

import pymongo				# mongodb interface
import datetime				# datetime package
import csv					# csv read/write
import StringIO				# read Strings as file

########   store.py   ##################
#
# A simple package to store data into the MongoDB instance running
# for the FinanPred service 

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
	print "store.py :: client successfully created"

# close global client connection
def closeClient():
	global client, db 		# prevent variable shadowing
	client.disconnect()
	client = db = None
	print "store.py :: client successfully destroyed"

# store a single entry vector to database
#	vec : the data vector to be stored
#	sym : the symbol to store data under
def storeEntry(vec, sym):
	entry = {
		"sym" : sym,
		"date" : vec[DATE_CL],
		"open" : vec[OPEN_CL],
		"high" : vec[HIGH_CL],
		"low" : vec[LOW_CL],
		"close" : vec[CLOSE_CL],
		"volume" : vec[VOLUME_CL]
	}
	db.historical_data.insert(entry)

######## DEFINE public functions #######

# store stock data into database
#	vals : the data to be stored (as a filestream)
# 	sym : the symbol to store data under
def storeHistData(data, sym):
	print "store.py :: Opening MongoDB Connection"
	openClient()
	lastDate = None;
	lastData = None;
	for line in data:
		vals = line.split(",")
		cDate = datetime.datetime.strptime(vals[DATE_CL], '%Y-%m-%d')
		vals[DATE_CL] = cDate;
		if lastDate is None:
			lastDate = cDate						# set date counter.
			lastData = vals							# set value vector. 
#		elif (lastDate - cDate) > datetime.timedelta(days=1)):
#			# fill in missing data
#			tDate = cDate + datetime.timedelta(days=1)
#			while (tDate != lastDate):
#				tvals = vals[:]
#				tvals[DATE_CL] = tDate
#				storeEntry(tvals, sym)				# store temporary vector
#				tDate += datetime.timedelta(days=1)	# increment time
		else:
			storeEntry(vals, sym)
		print "{} for {}".format(cDate, sym)
	print "store.py :: Closing MongoDB Connection"
	closeClient()

