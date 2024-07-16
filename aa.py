n = int(input().strip())
if(n%2!=0):
    print("Weired")
elif (n%2==0 and 2<=n<=5):
    print("Not Weired")
elif(n%2==0 and 6<=n<=20):
    print("Weired")
elif(n%2==0 and n>20):
    print("Not Weired")
   
