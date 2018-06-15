x=(5,3,5,)
x=tuple(x)
print(x)
print(len(x))
print(max(x))
print(min(x))
p=x[0]*x[1]*x[2]
print(p)


x1=int(input("enter a number:"))
x2=int(input("enter a number:"))
x3=int(input("enter a number:"))
x4=int(input("enter a number:"))
x5=int(input("enter a number:"))
x6=int(input("enter a number:"))
x=set([x1,x2,x3])
y=set([x4,x5,x6])
print(x-y)
print(x == y,x<=y,y<=x)
print(x&y)


#assignment q1
d={}
name=input("enter your name:")
marks=int(input("enter your marks:"))
d[name]=marks
name=input("enter your name:")
marks=int(input("enter your marks:"))
d[name]=marks
marks=int(input("enter your marks:"))
d[name]=marks
print(d)


# l=list(d.values())

x=["m","i","s","s","i","s","s","i","p","p","i"]
print(x.count("s"))











