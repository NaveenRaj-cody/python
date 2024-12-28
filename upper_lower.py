"""n=int(input())
s=20
for i in range(n):
    print(s-i,end=" ")
    s=s-i"""
    
s=input()
l=len(s)//2
a=s[:l].upper()
b=s[l:].lower()
print(a+b)
