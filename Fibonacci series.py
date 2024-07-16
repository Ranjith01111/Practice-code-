n = 10
num1 = 0
num2 = 1
next_n = num2
count = 1
while count <= n :
    print(next_n, end="  ")
    count += 1
    num1, num2, = num2, next_n
    next_n = num1 + num2
print()    
