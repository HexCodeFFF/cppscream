# this code is janky and so is my brain
# it SHOULD work with most c++ code, though it will be smaller if you space out as much as you can

code = open("input.cpp", "r").read()

achar = "A"
stringspace = "😋"  # doesnt matter as long as it doesnt appear in the program

reference = []  # index + 1 is number of As, no need for dict
out = ""

# fix strings
# i replace all spaces in strings with a random character to group them together for the defining code, then make them spaces again after defining is finished
instring = False
fixedcode = ""
for char in code:
    if char == "\"":
        instring = not instring
    elif char == " " and instring:
        char = stringspace
    fixedcode += char
ccode = fixedcode.split("\n")
# make define lines
for line in ccode:
    if line.startswith("#"):  # idk might remove later
        out += line + "\n"
    else:
        line = line.strip().split(" ")
        for piece in line:
            if piece not in reference:
                if "\"" in piece:
                    piece = piece.replace(stringspace, " ")
                reference.append(piece)
print(reference)
# write the defined code
# write define lines
for i, r in enumerate(reference):
    out += f"#define {achar * (i + 1)} {r}\n"

for line in ccode:
    if not line.startswith("#"):  # idk might remove later
        line = line.strip().split(" ")
        for piece in line:
            if "\"" in piece:
                piece = piece.replace(stringspace, " ")
            out += achar * (reference.index(piece) + 1) + " "
        out += "\n"

print(out)
open("output.cpp", "w+").write(out)
