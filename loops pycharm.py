x = "Hey there . How are you?"
for i in x:
    for j in i:
        if j==".":
            break
        print(j, end =" ")
print(i,end = " ")
print()
