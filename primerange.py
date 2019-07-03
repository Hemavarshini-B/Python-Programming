a=input().split()
b=int(a[0])
c=int(a[1])
for l in range(b+1,c+1):
  if l>1:
    for i in range(2,l):
      if l%i==0:
        break
    else:
      print(l,end=' ')
