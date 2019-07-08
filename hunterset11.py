n=int(input())
l=list(map(int,input().split()))[:n]
a=len(l)
l1=[]
for i in range(a):
  b=i+1
  for j in range(b,a):
    if l[i]==l[j] and l[i] not in l1:
      l1.append(l[i])
l1.sort()
if len(l1)==0:
    print("unique")
else:
    print(*l1,end=' ')
