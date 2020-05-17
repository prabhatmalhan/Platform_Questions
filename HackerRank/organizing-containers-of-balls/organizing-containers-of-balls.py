for _ in range(int(input())) :
	M = [list(map(int,input().split())) for i in range(int(input()))]
	print("Possible" if sorted([sum(i) for i in zip(*M)]) == sorted([sum(i) for i in M]) else "Impossible")