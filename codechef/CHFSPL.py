# cook your dish here
N= int(input())
for i in range(N):
    a=list(map(int, input().split()))
    a.sort()
    n = a[1] + a[2]
    print(n)
    
