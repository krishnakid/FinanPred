#!/usr/bin/env python

import requests				# HTTP request library
import json					# Python JSON library

########   load.py   ##################
#
# A simple toy script to load financial data in from Yahoo.  In the
# completed suite, this script will load from multiple sources and
# aggregate them into a single standardized format for analysis.

####### define CONSTANTS ##############

reqURL = "http://finance.yahoo.com/d/quotes.csv"


####### define METHODS   ##############

def loadData(vals):
	data={
		"s" : "+".join(vals),
		"f" : "snd1l1yr"
	}
	r = requests.get(reqURL, params=data)
	return r.text
