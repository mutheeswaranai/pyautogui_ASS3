


Name =["Muthees","Vasanth","Siva"]

print(Name)

print(Name[0]) #----first time start at 0---

Name.append("Kumar")  #----add New item

print(Name)

Name[1]="Yashiii" #change ---item---

print(Name)

#------------tuple()----------


colors=("red", "yellow","green")

print(colors)
print(colors[0]) #-----we can read items
                 #this  would given an Error  (Tupls cannot change  )

#--------Set { }----------

numbers={1,2,3,3,2}
print( numbers)  #---Duplicates are autometically removed ---
numbers.add(4)  #--- add new items
print(numbers)

#-------Dictionary {key: value }------


id={
    "Name":"Muthees",
    "Age":24,
    "City":"Theni"  

}
print (id)

print(id["Name"])

id["Age"]=25
print(id)
