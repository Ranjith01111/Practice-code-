def add(a,b) :
    return a+b
def sub(a,b) :
    return a-b
def mul(a,b) :
    return a*b
def div(a,b) :
    return a/b
def rem(a,b) :
    return a%b

a = int(input('Enter the number :'))
b = int(input('Enter the number :'))
ch = input()
if (ch == '+') :
    print(add(a,b))
elif (ch == '-') :
    print(sub(a,b))
elif (ch == '*'):
    print(mul(a,b))
elif (ch == '/'):
    print(div(a,b))
elif (ch == '%') :
    print(rem(a,b))
