n=int(input())
for i in range(n):
    z = list(map(int,input().split( )))
    x=set(z)
    if(len(x)==4):
        print(2)
    elif(len(x)==3):
        print(2)
    elif(len(x)==2):
        z.sort()
        y=z[0]
        if(z.count(y)==2):
            print(2)
        else:
            print(1)
    else:
        print(0)
