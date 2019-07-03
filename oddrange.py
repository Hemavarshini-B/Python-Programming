a=input().split()
b=int(a[0])
c=int(a[1])
for i in range(b+1,c):
  if(i%2!=0):
    print(i,end=' ')
