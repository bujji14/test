a=int(input())
b=1
temp=0
for i in range(0,a):
    if(i%2==0):
        while(a!=0):
            print(b,end=" ")
            b+=1
    else:
        while(a!=0):
            b=b+b-1
            print(b,end=" ")
            b-=1
    print(" ")
b=b+b+1



