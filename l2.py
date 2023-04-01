a=int(input("enter number of the station: "))
name_of_station=[]
day_of_the_week =[]
name_of_show =[]
for i in range(a):
    name=input()
    name_of_station.append(name)
for i in range(a):
    week=input()
    day_of_the_week.append(week)
for i in range(a):
    show=input()
    name_of_show.append(show)   
         
    
for i in name_of_station:   #traversinga list
    print(i)
for i in day_of_the_week:   #traversinga list
    print(i)
for i in name_of_show:   #traversinga list
    print(i)        
    
    
    