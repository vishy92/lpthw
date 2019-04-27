# just prints these strings
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do? 10 dots

# adds a string to vars
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# the comma here prints the next printout on the same line
# with a space after the last var
# use this to not go over 80 chars on a line!!
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)
# how to print with ''.join() on the same line? :thinking:
print(''.join((end1, end2, end3, end4, end5, end6)),)
print(''.join((end7, end8, end9, end10, end11, end12)))
