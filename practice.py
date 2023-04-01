'''l1=list('hello')
print(l1)
#l2=list(input("enter the elements: "))
l2=list("world")
print(l2)
l[4]="x"
print(l)
for i in l2:
    print(i)
l3=l1+l2 #concatenation
print(l3) 
l4=l3*3  #replication
print(l4)
print(l3[2:10:3]) #slicing
l3[0:2]=[0,1]  #list modification /update
print(l3)
l3.append("y") #append
print(l3)
del l3[0:4] #delete
print(l3)
del l3  #delete whole list
print(l3)
b=l3 #not true copy just placement
print(b)
c=list(l3) #true copy
print(c)'''

c=list("rudrika")
print(c)
x=c.count("r")
print(x)
c.sort()
print(c)
c.reverse()
print(c)
c.sort(reverse=True)
print(c)
