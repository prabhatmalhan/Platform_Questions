n, k = [int(e) for e in input().split()] 

lst = [int(e)%k for e in input().split()]

s = [0]* k

for i in lst:
    s[i] += 1
    
c = 0
    
for i in range(1,k//2+1):
    c += max(s[i],s[k-i])

c += min(s[0],1)

if k%2==0:
    c-=s[k//2]-1

print(c)
