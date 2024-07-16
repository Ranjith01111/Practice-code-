row = int(input("Enter the row : "))
col = int(input("Enter the colomns : "))
x = []
b = []
print("First matrix :-")
for i in range(0,row):
    for j in range(0,col):
        b.insert(j,int(input("Enter the value %d * %d : " %(i,j))))
    x.insert(i,b)
    b = []
y = []
print("Second matrix :-")
for i in range(0,row):
    for j in range(0,col):
        b.insert(j,int(input("Enter the value %d * %d : " %(i,j))))
    y.insert(i,b)
    b=[]
su = []
print("Output matrix :-")
for i in range(0,row):
    for j in range(0,col):
        b.insert(j, x[i][j]+y[i][j])
    su.insert(i,b)
    b=[]
print(su)
