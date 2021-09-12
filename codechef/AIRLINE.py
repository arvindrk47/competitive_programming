# cook your dish here
n = int(input())
while(n):
    a,b,c,d,e = map(int, input().split(' '))
    if (a+b<=d and c<=e):
        print("Yes")
    elif (a+c<=d and b<=e):
        print("Yes")
    elif(b+c<=d and a<=e):
        print("Yes")
    else:
        print("No")
    n-=1
