import random
check = False
print("test")
while check is False: 
    Userinput = input()
    input = int(Userinput)
    check = input >= 0 and input <= 9
    if check is False: 
        print("please print correct number")
    else: 
        check = True

randint = random.randint(0,9)
if(input > randint):
    print("you win")
else: 
    print("you lose")