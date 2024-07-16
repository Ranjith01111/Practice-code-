n = int(input('Enter the number :'))
e = 0
eo = 0
while n>0 :
    d = n%10
    if ((d%2) == 0) :
        e = e+d
    else :
        eo = eo+d
    n = n//10
print('sum of even digit ' , e)
print('sum of odd digit ' ,eo)
