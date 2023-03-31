for _ in range(int(input())):
    n=int(input())
    s=input()
    count=0
    a=['a','e','i','o','u']
    for i in s:
        if i in a:
            break
        else:
            count+=1
    if(count>4):
        print('NO')
    else:
        print('YES')