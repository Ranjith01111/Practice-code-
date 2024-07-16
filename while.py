import random
nump = random.randint(1000,9999)
print(nump)
n = int(input("Enter the number : "))
while n != 10 :
    num = nump
    cor = 0
    while num%10 :
        numc = num%10
        nc = n%10
        num = num//10
        n = n//10
        if numc==nc:
            cor = cor+1
    if cor==4:
        print("Congrats , You will finded")
        break
    else :
        print("%d you guesses right" %cor)
        n = int(input("Enter the number : "))
else :
    print("You quite the game")
