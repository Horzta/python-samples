# Creating Lists
pet_names = ["Oreo", "Spike", "Jam"]
pet_ages = [7,2,1]
pets = [["Oreo", 7], ["Spike", 2], ["Jam", 1]]

# Printing Lists
print(pet_names[0])#Oreo
print(pet_names[0:2])#['Oreo', 'Spike']
print(pet_names[-1])#Jam
print(pets[1][0])#Spike
print(pet_names)#['Oreo', 'Spike', 'Jam']

# List length
pets_length = len(pets)
print(pets_length) #3

# Editing list object
pet_names[0] = "Moreo"
print(pet_names) #['Moreo', 'Spike', 'Jam']

#Appending to lists
pet_names.append("Jake")
print(pet_names) #['Moreo', 'Spike', 'Jam', 'Jake']

#Inserting to Lists
pet_names.insert(1,"Bubblegum")
print(pet_names) #['Moreo', 'Bubblegum', 'Spike', 'Jam', 'Jake']

# Removing from Lists
pet_names.remove("Moreo")
print(pet_names) #['Bubblegum', 'Spike', 'Jam', 'Jake']

# Popping from lists
pet_names.pop()
print(pet_names) #['Bubblegum', 'Spike', 'Jam']
pet_names.pop(1)
print(pet_names) #['Bubblegum', 'Jam']

# Clearing the Lists
pet_names.clear()
print(pet_names) #[]