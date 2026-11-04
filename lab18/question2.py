#D= dict( [ ('first' , '1') , ('second' , '2') , ('third' , '3') , ('fourth' , '4') , ('fifth' , '5') ] )
#sum=0
#values=D.values:
#for i in values 8:


D= { "First": 1 , "Second": 2 , "Third": 3 , "Fourth": 4 , "Fifth": 5 , "Sixth": 6 }
values=D.values()
total = 0
for i in values:
    total = total + i

print(total)

