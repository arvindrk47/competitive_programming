# cook your dish here
n=int(input())
for i in range(n):
    a=int(input())
    if a<1600:
        print(3)
    elif 2000<=a:
        print(1)
    else:
        print(2)
