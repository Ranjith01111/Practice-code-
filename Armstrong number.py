n = int(input('Enter the number :'))
i = 0
t = n
while t>0 :
    d = t%10
    i = i+d**3
    t = t//10
if n==i  :
    print (n,"is a Armstrong number")
else :
    print (n,"is not a Armstrong number")























