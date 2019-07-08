a=int(input())
l=list(map(str,input().split(" ")))
l.sort()
b=l[::-1]
c="".join(map(str,b))
num=int(c)
print(c)
