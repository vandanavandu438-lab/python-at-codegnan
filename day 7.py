#find the largest number amoung three numbers
n1=int(input())
n2=int(input())
n3=int(input())
if n1>n2:
    if n1>n3:
        print(f"{n1} is greater")
    else:
        print(f"{n3} is greater")
else:
    if n2>n3:
        print(f"{n2} is greater")
    else:
        print(f"{n3} is greater")
