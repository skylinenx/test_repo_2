#string
name = "Nisal"
print(name[0]) #N

#list
names = ["Nisal", "Sandy", "Sky"]
print(names)    #['Nisal', 'Sandy', 'Sky']
print(names[0])     #Nisal
print(names[1][0])  #S

names.append("Mittens") #added to the end of list
names.remove("Sky")
names.sort() #sort alphebetically
print(names) #['Mittens', 'Nisal', 'Sandy']
print(f"items in names list: {len(names)}")

#tuple
cordinates = (20.5, -56.3)
print(cordinates)   #(20.5, -56.3)
print(cordinates[0])    #20.5

#set
s = {10,20}
s.add(10)
s.add(30)
s.remove(30)
print(s)    #{10, 20}

#dict
owner_car = {
    "Nisal": "Civic",
    "Sandy": "Alto",
    "Thara": "Corolla"
}
print(owner_car) #{'Nisal': 'Civic', 'Sandy': 'Alto', 'Thara': 'Corolla'}
print(owner_car["Sandy"]) #Alto

#add new pairs
owner_car["Mittens"] = "4 legs"