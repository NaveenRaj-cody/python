n=int(input())
p=n**2
s=str(p)
l=len(s)//2
a=int(s[0:l])
b=int(s[l:])
if(a+b==n):
    print("It is kaprekar")
else:
    print("It is not kaprekar")
