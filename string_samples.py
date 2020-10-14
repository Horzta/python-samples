# Creating strings
var1 = "Hello World"
var2 = '111 Roxas Ave' 

# Printing strings
print("var1: " + var1) #var1: Hello World
print("var2: " + var2) #var2: 111 Roxas Ave

# Concatenating Strings
var3 = var1 + var2
var4 = "Greetings:{} Address:{}".format(var1, var2)
print("var3: " + var3) #var3: Hello World111 Roxas Ave
print("var4: " + var4) #var4: Greetings:Hello World Address:111 Roxas Ave

# Accessing Strings
# var[start:end]
print("var1[0]: " + var1[0]) #var1[0]: H
print("var2[4]: " + var2[4]) #var2[4]: R

print("var1[-1]: " + var1[-1]) #var1[-1]: d
print("var1[-3]: " + var1[-3]) #var1[-3]: A

print("var1[0:5]: " + var1[0:5]) #var1[0:5]: Hello
print("var2[4:9]: " + var2[4:9]) #var2[4:9]: Roxas

# var[start:end:step]
var5 = "123456789"
print("var1[0:99:2]: " + var5[0:99:2]) #var5[0:99:2]: 13579
