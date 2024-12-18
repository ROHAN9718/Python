import random
color=["red","green","blue"]
print(color)
print("vartual wallet:1000".center(150," "))
a=(random.choice(color))
r=input("select anyone")
if (r==a):
    print("you won")
    print("answer is",a)
    print("you are eligible for next level")
    print(("do you want to play next level:\n1)yes\n2)No"))
    t=input("CONTINUE: ")
    if(t=="yes" or t=="Yes" or t=="1" or t=="y"):
        print("level 2")
        print('choose a color'.center(50))
        print("\n1)red\n2)green\n3)blue")
        c=input("select: ")
        c=c.lower()
        y=random.choice(color)
        if(y==c):
            print("you won")
            print("wllet:200".center(180," "))
        else:
            print("you lose")
        print("Answer is",y)
    else:
        print("thankyou for playing")
    
else:
    print("you lose")
    print("answer is",a)
    print(("do you want to play next level:\n1)yes\n2)No"))
    t=input("CONTINUE: ")
    if(t=="yes" or t=="Yes" or t=="1" or t=="y"):
        print("level 2")
        print('choose a color'.center(50))
        print("\n1)red\n2)green\n3)blue")
        c=input("select: ")
        c=c.lower()
        y=random.choice(color)
        if(y==c):
            print("you won")
            print("wllet:200".center(180," "))
        else:
            print("you lose")
        print("Answer is",y)
    else:
        print("thankyou for playing")