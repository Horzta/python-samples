
# For loop
favorite_people = ["Lady", "Mark", "Fred", "Gary", "Christian", "Clint"]
for person in favorite_people:
    print("I like " + person)
print("----------------------------------------")

for number in range(2,20,2):
    print("{} is an even number.".format(number))
print("----------------------------------------")

for cat_sound in ["Swswswsw", "Mewmewmew", "Meow Meow"]:
    print("{} is a cat sound".format(cat_sound))
print("----------------------------------------")

# While loop
levels = [1,2,3,4,5]
level_index = 0
while level_index != 5:
    print("Level {}".format(levels[level_index]))
    level_index = level_index + 1
print("----------------------------------------")
