print("I will now count my chickens:")

print("Hens", 25.0 + 30.0 / 6.0)

# % and * have identical priority so do from left to right. - is lower priority so...
# 3 * 25 = 75 >>> 75 % 4 = 3 >>> 100 - 3 = 97
print("Roosters", 100.0 - 25.0 * 3.0 % 4.0)

print("Now I will count the eggs:")

# 4 % 2 = 0 and 1 / 4 = 0 too because without a decimal place it's a non-floating point
# number so it only deals in whole numbers...
# 6 - 5 + 0 - 0 + 6 = 7
print(3.0 + 2.0 + 1.0 - 5.0 + 4.0 % 2.0 - 1.0 / 4.0 + 6.0)

print("Is it true that 3 + 2 < 5 - 7?")
# answer, gives back true or false
print(3.0 + 2.0 < 5.0 - 7.0)
# simplifies why the above gave back false.
print("What is 3 + 2?", 3.0 + 2.0)
print("What is 5 - 7?", 5.0 - 7.0)
# duh
print("Oh, that's why it's False.")
# fk me
print("How about some more.")
# more info about the previous question. gives back True or False
print("Is it greater?", 5.0 > -2.0)
print("Is it greater or equal?", 5.0 >= -2.0)
print("Is it less or equal?", 5.0 <= -2.0)
