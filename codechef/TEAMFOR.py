# cook your dish here
n=int(input())
for i in range(n):
    le=int(input())
    a=input()
    b=input()
    c=a.count('1')
    d=b.count('1')
    print(min(c,d,le//2))
