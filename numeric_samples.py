#Creating Numeric
var_i = 10
var_f = 10.5
var_i2 = 5
var_f2 = 5.0

# Checking types
print(type(var_i)) #<class 'int'>
print(type(var_f)) #<class 'float'>
print(type(var_i2)) #<class 'int'>
print(type(var_f2)) #<class 'float'>

# Number operations
var_sum_i = var_i + var_i2 # 15
var_dif_i = var_i - var_i2 # 5
var_pro_i = var_i * var_i2 # 50
var_quo_i = var_i / var_i2 # 2.0
var_mod_i = var_i % var_i2 # 0

var_sum_f = var_f + var_f2 # 15.5
var_dif_f = var_f - var_f2 # 5.5
var_pro_f = var_f * var_f2 # 52.5
var_quo_f = var_f / var_f2 # 2.1
var_mod_f = var_f % var_f2 # 0.5

# Mixed Type Operations
var_sum_m = var_f + var_i2 # 15.5
var_dif_m = var_f - var_i2 # 5.5
var_pro_m = var_f * var_i2 # 52.5
var_quo_m = var_f / var_i2 # 2.1
var_mod_m = var_f % var_i2 # 0.5

# Other operations
expo = 5 ** 2 # 25
floor = 10 // 3 # 3

print(expo)
print(floor)