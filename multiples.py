#MULTIPLES OF A NUMBER

n = int(input())
start = int(input())
end = int(input())
count = 0
for i in range(start, end+1):
    if i%n == 0:
        print(i, "multiple of", n)
        count = count+ 1
print("Total number of multiples from start to end is : ", count)
