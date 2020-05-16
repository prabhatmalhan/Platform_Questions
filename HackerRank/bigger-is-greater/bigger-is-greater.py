def fun(s) :
    for i in range(len(s)-1)[::-1]:
        if s[i] < s[i+1]:
            for j in range(i+1,len(s))[::-1]:
                if s[i] < s[j]:
                    lis = list(s) 
                    lis[i],lis[j]=lis[j],lis[i]
                    return "".join(lis[:i+1]+lis[i+1:][::-1])
    return 'no answer'
    
T = int(input())
for i in range(0,T):
    print(fun(input()))
