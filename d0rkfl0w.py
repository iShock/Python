import urllib2
import sys
from os import system



def main():
	if init() == 255:
		return;


def init():
	print "Calling a function!"
	option = raw_input("Digite uma opção entre[%s]:" % total_otp)

	if "0" in option:
		print "0"
	if "q" in option:
		print "\nFechando aplicativo...!\n\n"
		exit()
	if "Creditos" in option:
		cCreditos()
	return init();


if __name__ == "__main__":
	main()