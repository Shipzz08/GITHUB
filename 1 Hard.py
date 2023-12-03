def find(num):
    nat_num=[]
    for i in range(1,num+1):
        nat_num.append(i)
    sum=0
    for n in nat_num:
        while(n>0):
            d=n%10
            if(d==1):
                sum+=1
            n=n//10
    print(sum)
    
number=int(input())
find(number)

