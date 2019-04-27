types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"  # 1
do_not = "don't"  # 2
# sets a var to a string with 2 embedded format strings
y = f"Those who know {binary} and those who {do_not}."

print(x)  # 5?
print(y)  # 6?

print(f"I said: {x}")  # 3
print(f"I also said: '{y}'")  # 4
# you can add the content of a format string at print
hilarious = True
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."
# you can add variables together. + concatenates strings
# if adding more than 2 use ''.join()
print(w + e)
print(''.join((w, e)))
