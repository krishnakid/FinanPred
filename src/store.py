#!/usr/bin/env python

from consts import *		# local constants header

import pymongo				# mongodb interface
import datetime				# datetime package
import csv					# csv read/write
import StringIO				# read Strings as files

########   load.py   ##################
#
# A simple package to store data into the MongoDB instance running
# for the FinanPred service 


# store stock data into database
#	vals : the data to be stored (as a filestream)
# 	sym : the symbol to store data under
def storeHistData(data, sym):
	for line in data:
		vals = line.split(",")
		print "{} for {}".format(datetime.datetime.strptime(vals[DATE_CL],
															 '%Y-%m-%d'), sym)
