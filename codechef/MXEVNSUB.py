# cook your dish here
for i in range(int(input())):
    a = int(input())
    sum = (a*(a+1))//2
    if (sum%2 ==0):
        print(a)
    else:
        print(a-1)
