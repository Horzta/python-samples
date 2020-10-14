# Creating a dictionary
a_dictionary = {
    "name": "Akira Hora",
    "age": 18,
    "job": "Software Developer"
}

# Accessing a Dictionary
print(a_dictionary)
print(a_dictionary["name"])
print(a_dictionary.get("job"))
print("----------------------------------------")

# Setting a property
a_dictionary["age"] = 20
print(a_dictionary.get("age"))
print("----------------------------------------")


for keys in a_dictionary:
    print(keys)
print("----------------------------------------")

for values in a_dictionary.values():
    print(values)
print("----------------------------------------")

for key, value in a_dictionary.items():
  print(key, value)
print("----------------------------------------")

if "name" in a_dictionary:
    print("In dictionary")
else:
    print("Not in dictionary")
print("----------------------------------------")
