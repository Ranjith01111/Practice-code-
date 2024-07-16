pwd = input("enter a password:")
if(pwd.islower()==False and pwd.isupper()==False):
    if (pwd.isalnum()==False) and ('@' in pwd) or ('#' in pwd) or ('.' in pwd)or( '&' in a):
        if(len(pwd)>=8):
            print("Valid password and strong")
        else:
            print("Valid but not strong")
    else:
        print("does not contain any special characters")
else:
    print("contain only lower and upper ")

