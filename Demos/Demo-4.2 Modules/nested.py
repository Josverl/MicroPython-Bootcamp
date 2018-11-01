""" 
my module with a submodule
"""
import myprinter

def dowork(x,y):
	return x+y

def greet(n):
	m = 'hello'+str(n)
	return m

def greetit(name):
	myprinter.printit(greet(name))
