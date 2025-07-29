#String Manipulation

text = "Turn on the lights!"

lower = text.lower()
print(lower)

replace = text.replace("!", ".")
print(replace)

split = text.split()
print(split)

split[1] = "off"
split_off = split
print(split_off)

text_join = " ".join(split_off)
print(text_join)

check = "lights" in text
print(check)

#String Manipulation

#Regular Expressions

import re

text = "Play song number 45"

match = re.search("\d+", text)
match2 = re.search("song", text)
print(match)
print(match2)

match3 = re.findall("\w*", text)
print(match3)


#Regular Expressions


#File I/O

with open("lambdatext.txt", "r") as f:
    lines = f.readlines()

with open("lambdatext2.txt", "w") as f:
    f.write = ("\n".join(lines))

#File I/O





