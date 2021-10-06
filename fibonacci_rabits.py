list_range = int(input("Enter no (n)"))
k = int(input("Every pair of reproduction-age rabbits produces a litter of how many rabbit pairs: "))

f1 = 0
f2 = 1
f3 = 1

fib_list = [f2, f3]

for x in range (0,list_range-2):
    num = f3 + f2*k
    f2 = f3
    f3 = num
    fib_list.append(num)

print(fib_list)
print("The total number of rabbit pairs that will be present after n months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs is: ",fib_list[-1])
