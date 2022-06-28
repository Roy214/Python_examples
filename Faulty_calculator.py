# !/usr/bin/env python3
print("Enter first number")
n1 = int(input())
print("Enter second number")
n2 = int(input())
print("Choose the arithmetic operation you would like to perform\n a. Add \n b. Subtract \n c. Multiple \n d. Divide")
opt = str(input())
if opt == 'a':
    if n1 != 56 and n2 != 9:
        res = n1 + n2
        print(res)
    else:
        print("Denied!! you are caught!!")
elif opt == 'b':
    res = n1 - n2
    print(res)
elif opt == 'c':
    if n1 != 45 and n2 != 3:
        res = n1 * n2
        print(res)
    else:
        print("Denied!! you are caught!!")
elif opt == 'd':
    if n1 != 56 and n2 != 6:
        res = n1 /n2
        print(res)
    else:
        print("Denied!! you are caught!!")
else:
    print("Choose a valid option")

