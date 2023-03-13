import random

def gameplay():
    one = random.randint(0,1);
    two = random.randint(0,1);
    thr = random.randint(0,1);
    fre = random.randint(0,1);
    fiv = random.randint(0,1);
    six = random.randint(0,1);

    list1 = [one,two,thr,fre,fiv,six]
    num = []

    for num in list1:
 
        # checking condition
        if num == 0:
            num = "🔺"
 
        else:
            num = "🔻"
        print(num,end=" ")

while True:
    a = input("Enter y/n to continue ")
    if a=="y":
        gameplay()
        continue
    elif a=="n":
        break
    else:
        print("Enter either yes/no")
