# cook your dish here
n= int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    features = set(arr[:2])
    a=set(arr[2:4])
    b=set(arr[4:6])

    if (features == a):
        print(1)
    elif(features == b):
        print(2)
    else:
        print(0)
