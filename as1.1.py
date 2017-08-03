# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT

#import random

lines = []
print "Enter sequence of lines: "

while True:
	line =  parseInt.input("> ")
	if not line:
		break
	lines.append(line.upper())
#for sentence in lines:
print lines