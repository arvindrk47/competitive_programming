# cook your dish here
n = int(input())
while(n):
    a,b,c = map(int, input().split(' '))
    s = input()
    res = s.count('0')*b + s.count('1')*c
    print(res)
    n-=1
