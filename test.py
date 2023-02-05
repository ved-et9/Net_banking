x=int(input())
for i in range(x):
    y=int(input())
    p=list(map(int,input().split()))
    c=list(map(int,input().split()))
    
    answer=0
    count=0
    list1=[]
    for i in range(y):
        list1.append(p[i]+c[i])
    greatestp=0
    greatestc=0        
    for t in range(y):
        if p[t]>greatestp:
            greatestp=p[t]
            answer=t

    for t in range(y):
        if p[t]==greatestp:
            count=count+1
    if count!=1:
        for i in range(y):
            if greatestc<list1[i]:
                greatestc=list1[i]
                answer=i

    print(answer+1)    


