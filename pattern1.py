a=int(input())
b=1
temp=0
for i in range(0,a):
    if(i%2==0):
        for j in range(0,a):
            print(b,end=" ")
            b+=1
        temp=b+a-1
    else:
        for j in range(0,a):
        
            print(temp,end=" ")
            temp-=1
        
    print()
    b=temp+a+1



