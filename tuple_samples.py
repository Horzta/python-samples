# Creating Tuples
pet_names = ("Oreo", "Spike", "Jam")
pet_ages = (7,2,1)
pets = (("Oreo", 7), ("Spike", 2), ("Jam", 1))

# Printing Tuples
print(pet_names[0])#Oreo
print(pet_names[0:2])#('Oreo', 'Spike')
print(pet_names[-1])#Jam
print(pets[1][0])#Spike
print(pet_names)#('Oreo', 'Spike', 'Jam')

# Tuples length
pets_length = len(pets)
print(pets_length) #3
