from math import ceil,floor
str = list("".join(input().split()))
l=len(str)
r,c = list(map(int,[floor(l**.5),ceil(l**.5)]))
for i in range(c) :
	for j in range(r):
		a = j*c+i
		if a<l : print(str[a],end = "")
	print()