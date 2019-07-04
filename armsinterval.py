a,b=map(int,input().split())
for i in range(a,b+1):
  ord=len(str(i))
  sum=0
  tmp=i
  while tmp>0:
    digit=tmp%10
    sum=sum+digit**ord
    tmp=tmp//10
  if i==sum:
    print(i)
