import random
p = input("Enter your name : ")
print("Welcome sir "+ p)
password=input("Enter the password : ")
if password=="zero-day":
    u=input("Does the victim mean anything to you? : ")
    a=input("Enter the victim's name : ")
    r=int(input("Enter the number of passwords required : "))
    w=9
    g=a
    x=0
    while True:
        pas="".join(random.sample(g,w))
        print(pas)
        x+=1

        if x==r:
            break
else :
    print("wa ta sir t9awed")
