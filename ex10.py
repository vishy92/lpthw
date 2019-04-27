# tabs in
tabby_cat = "\tI'm tabbed in."
# prints on a new line
persian_cat = "I'm split \n on a line."
# just a backslash
backslash_cat = "I'm \\ a \\ cat."
# just tabbed in strings
fat_cat = '''
I'll do a list:
\t* Cat Food
\t* Fishies
\t* Catnit\n\t* Grass
'''

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# Do more practice using the same lyrics form the last ex.

lyrics = "It starts with one\nOne thing, I don't know why \
\nIt doesn't even matter how hard you try\nKeep that in mind\n {}"

print(lyrics.format('''
    \tOkay.
    \tThats enough.
    \tThank you Mike!
'''))
