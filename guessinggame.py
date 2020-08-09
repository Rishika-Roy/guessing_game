import random

a=random.randrange(1,101)
#print(a)

b=int(input("enter the number:"))
if a==b:
    print("you found the number")
else:
    while a!=b:

        if a> b:
            print("the number is higher")
            b=int(input("enter the number again:"))
            if a==b:
                print("you found the number")
        elif a< b:
            print("the number is lower")
            b=int(input("enter the number again:"))
            if a==b:
                print("you found the number")
    
