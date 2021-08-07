# cook your dish here
n=int(input())
for i in range (n):
    a,b,c,d,e,f = map(int, input().split())
    x=a+b+c;
    y=d+e+f;
    if x>y:
        print(1)
    else:
        print(2)
