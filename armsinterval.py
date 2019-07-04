a,b=map(int,input().split())
for i in range(a,b+1):
  sum=0
  tmp=i
  while tmp>0:
    digit=tmp%10
    sum=sum+digit**3
    tmp=tmp//10
  if i==sum:
    print(i,end=' ')
