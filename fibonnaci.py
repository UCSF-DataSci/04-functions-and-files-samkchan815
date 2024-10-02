#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. 
The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""
import argparse

def fibonacci_seq(output, max):
	'''Return Fibonacci sequence numbers as a list in an output file'''

	seq = [0, 1]
	curr = 1

	while (curr < max):
		seq.append(curr)
		curr = seq[-1] + seq[-2]
	
	outputFile = args.output
	with open(outputFile, 'w') as file:
		file.write(str(seq))

	return seq

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-o", "--output", type=str, help="Output file name")
	parser.add_argument("-l", "--limit", type=int, default=100, help="Upper limit of Fibonacci sequence")
	args = parser.parse_args()

	fibonacci_seq(args.output, args.limit)