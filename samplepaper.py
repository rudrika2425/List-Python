t=eval(input())
outer=t[0]
inner=t[1]
flag=0
for i in inner:
    if i not in outer:
        flag=1
if(flag==1):
    print("false")
else:
    print("true")            