x = input("Enter the Email id : ")
x = x.lower()
print(x)
if (x.endswith('@gmail.com') or x.endswith('.in')) :
    print('Email Id is valid')
else :
    print('Email Id is invalid')
