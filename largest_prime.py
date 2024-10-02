#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

import fibonnaci
import argparse

def prime_num(num):
	'''Determine if number is prime or not'''
	for i in range(2, num): # start from 2 to input number bc 0 and 1 are prime
		if num % i == 0: # if divisible by i return false because not prime
			return False
	return True # else return true

def largest_prime(max):
	'''Find largest prime number in Fibonnaci sequence less than inputted max.'''
	seq = fibonnaci.fibonacci_seq(max) # get fibonnaci sequence less than max

	for i in reversed(seq): # reverse seq
		if prime_num(i) == True: #find first prime number is reverse sequence
			print(i) # print largest prime Fibonacci number
			break
	return None

if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	parser.add_argument("-m", "--max", type=int, default=100, help="Upper limit of Fibonacci sequence")
	args = parser.parse_args()

	largest_prime(args.max)

	# To find the largest prime Fibonacci number less than 50,000 please use the following
	# line of code in the command line:

	# python3 ./largest_prime.py -m 50000