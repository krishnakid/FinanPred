#!/usr/bin/env python

from consts import *

import numpy


########   predict.py   ##################
#
# The core implementation module of the FinanPred project.  Implements a 
# vanilla Neural Network that takes a set of training data, then can be used
# to predict future stock paths.
#
# initially implements a multilayer feed-forward perceptron network with a
# single hidden layer
#

####### define CONSTANTS ##############

nInput = 15									# number of input nodes
nHidden = 27								# number of hidden nodes
nOutput = 4									# number of output nodes

_alpha = 0.3								# learning rate

####### define GLOBALS ##############





####### define FUNCTIONS ##############

# trains a multilayer feedforward perceptron network
#	input :	the input data matrix 
#	expOut : the expected output data matrix
def trainNetwork(input, expOut):
	print "training network dummy"

# runs trained prediction algorithm on input vector
#	vec : the input vector to run
def predict(vec):
	print "prediction dummy"


















