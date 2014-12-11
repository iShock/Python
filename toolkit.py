#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib2
import sys
from os import system



total_otp = "1~5"


def main():
	if init() == 255:
		return; 
		
def init():	

	option = 0
	print "+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-"
	print "1:*Vulnerability scanner"
	print "2:*Hash tools"
	print "3:*Misc functions"
	print "4:*Credits"
	print "+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-+--+-+-+-"	
	
	print "\t\t\t\t\t\t\tDigite (q)uit para sair!"
	option = raw_input("Digite uma opção entre[%s]:" % total_otp)
	
	if "0" in option:
		print "0"
	if "q" in option:
		print "\nFechando aplicativo...!\n\n"
		exit()
	if "Creditos" in option:
		cCreditos()
	return init();

def cCreditos():
	print "Author: iShock"
	print "Version: 0.1a\n"

		
		
if __name__ == "__main__":
    main()

