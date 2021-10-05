#!/usr/bin/env python3

def Fibo(num):
	if num > 1:
		res = Fibo(int(num)-1) + Fibo(int(num)-2)
		return res

	elif num == 1:
		return 1
	elif num == 0:
		return 0
	
number = int(input("Enter number: "))

print(Fibo(number))

