n=int(input())
s=n*n
d=0
g=0
while(n>0):
    r=n%10
    d=d*10+r
    n=n//10
a=d*d
while(a>0):
    f=a%10
    g=g*10+f
    a=a//10
if(s==g):
    print('True')
else:
    print('False')