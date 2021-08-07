# cook your dish here
N = int(input())
for i in range(N):
    a,b,c = map(int, input().split())
    if a+b+c==0 or a+b+c ==3:
        print(0)
    else:
        print(1)
