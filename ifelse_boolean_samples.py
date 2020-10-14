# Booleans
condition1 = True
condition2 = True
condition3 = False


# Simple if
if True:
    print("A simple if statement")
print("----------------------------------------")

#Simple If-Else
if False:
    print("It will not go here")
else:
    print("A simple else statement")
print("----------------------------------------")

#Simple If-elif-else
if condition1 and condition2 and condition3:
    print("All conditions are true")
elif condition1 and condition2:
    print("conditiona1 and condition2 are true")
elif condition2 and condition3:
    print("conditiona2 and condition3 are true")
elif condition3 and condition1:
    print("conditiona3 and condition1 are true")
else:
    print("One or none is true")
print("----------------------------------------")

#Simple If-elif-else
if condition1 or condition2 or condition3:
    print("Either condition1, condition2 or condition3 is true")
else:
    print("None is true")
print("----------------------------------------")
