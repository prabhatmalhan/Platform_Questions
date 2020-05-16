def con(s): return int(s)

t=int(input())
a=1
while(a<=t):
    n,d=list(map(con,input().split()))
    x=list(map(con,input().split()))
    move_day=d
    for day in x[::-1]:
        move_day=move_day//day*day
    print(f'Case #{a}: {move_day}')
    a+=1