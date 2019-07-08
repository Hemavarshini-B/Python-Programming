a=int(input())
l=list(map(int,input().split(" ")))
tmp=0
for i in range(a):
	if i==l[i]:
		tmp=1
		print(i,end=" ")
if tmp==0:
	print("-1")
