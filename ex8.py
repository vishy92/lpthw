formatter = "{} {} {} {}"
# no quotes for ints
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
# no quotes for booleans
print(formatter.format(True, False, False, True))
# no quotes for vars
print(formatter.format(formatter, formatter, formatter, formatter))
# clearer formatting
print(formatter.format(
    "No light in the distane",
    "We were shadows holding on",
    "Holding on...",
    "All the things I resisted"
))
# experiment on how to print the lyrics on different lines:
# illenium btw :F

# formatter = "{}\n{}\n{}\n{}" this will print everything on a new line
# \n, '''

# practice (LP - In the end)
lyrics = "{}\n{}\n{}\n{}\n{}\n{}"

print(lyrics.format(
    "It starts with one",
    "One thing, I don't know why",
    "It doesn't even matter how hard you try",
    "Keep that in mind",
    "I designed this rhyme to explain in due time",
    "Random"
))
