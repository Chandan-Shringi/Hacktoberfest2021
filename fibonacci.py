#!/usr/bin/env python3

num = int(input("Enter number: "))
num_list = [0, 1, 1]
n0 = 0
n1 = 1
n2 = 1

for n in range(2, num):
	n3 = n2 + n1
	num_list.append(n3)
	n1 = n2
	n2 = n3
	
print(num_list)
print(num_list[-1])
