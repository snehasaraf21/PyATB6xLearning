shopping_list = ["bread","butter","paner"]
shopping_list[2]="milk"
print(shopping_list)


#real ex of tuples
my_tuples = ("tta.com","sdet.live")
print(my_tuples)#()
my_api_list = list(my_tuples)#list converts tuple to list as list is mutable(can be changed) but tuple cannot be (immutable)
print(my_api_list)#[]
my_api_list2= tuple(my_tuples)#conerts back list to tuple
print(my_api_list2)
print(my_api_list.append("item"))#none as it doesnt return anthing

t = tuple()#empty tuple can be created
print(t)

l=list()#empty list can be created
print(l)

#conerting tuple to list or vice versa can be done
t1= tuple(["Sneha",2,1.3,"Amit"])
print(t1)

hero1 = ("Sneha","Amit")
hero2= ("Vedant","Ritvi")
new_tuple = (hero1,hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[0][1])
print(new_tuple[1][1])