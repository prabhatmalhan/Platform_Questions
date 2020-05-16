t=int(input())
a=1
while(a<=t):
    n=int(input())
    h=input().split()
    for i in range(n):
        h[i]=int(h[i])
    c=0
    for i in range(1,n-1):
        if(h[i-1]<h[i]>h[i+1]):
            c+=1
    print('Case #' + str(a) + ': ' + str(c))
    a+=1