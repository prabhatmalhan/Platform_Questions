m = int(input())

scores = list(map(int,input().split()))

scores = sorted(set(scores),reverse = True)
m=len(scores)

n = int(input())

alice = list(map(int,input().split()))

for score in alice:
    if score >= scores[0] :
        print (1)
    elif score == scores[-1] :
        print (m)
    elif score < scores[-1] :
        print (m+1)
    else :
        b=0
        e=m-1
        while(b<=e) :
            mid=(b+e)//2
            if(scores[mid] == score):
                print (mid+1)
                break
            elif(scores[mid] > score):
                if(scores[mid+1] < score):
                    print (mid+2)
                    break
                b = mid + 1
            else:
                if(scores[mid-1] > score):
                    print (mid+1)
                    break
                e = mid - 1
