#!/bin/python2.7
##Paul's E-Time Calculator
##
##Created in Python 2.7.9
##
##
import math
print('\n''\n'"___________________________Paul's E-Time Calculator_____________________________"'\n''\n')


intime = input('What is your current total?   ')

while intime<0:
	print("Invalid input")

	intime = input('What is your current total?   ')


if intime>40:
	print("You are currently over the 40 hour limit.")


else:
	timeleft = (40-intime)

	hourleft = timeleft

	hourleftint = int(hourleft)

	timeleftmin = timeleft*60

	minleft = int(timeleftmin%60)

	print'\n''\n''You need to work another', timeleft ,'hour(s) to hit 40.''\n';

	print'\n''\n''That would be another', hourleftint ,'hour(s) and',minleft,'minute(s)!''\n''\n';

endpro = raw_input('Press Enter to Exit.')
