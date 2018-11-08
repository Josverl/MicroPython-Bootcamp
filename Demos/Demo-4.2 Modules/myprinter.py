""" 
my pretty printer module
"""

def printit(text):
	# use ANSI escape sequeences top print inverted, bold ,red text
	# https://en.wikipedia.org/wiki/ANSI_escape_code#3/4_bit
	print("\033[;7m\033[1;31m{}\033[0;0m".format(str(text) ) )

