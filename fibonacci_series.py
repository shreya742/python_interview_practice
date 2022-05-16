#Fibonacci Series

n = int(input())
n1, n2 = 0, 1
count = 0
if n < 0:
    print("please enter a valid number.")
elif(n == 1):
    print("Fibonacci series : "+n1)
else:
    while(count < n):
        print(n1)
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count += 1

"""
Add the current number with previous number.

OUTPUT : 0 1 1 2 3 5 8
"""
