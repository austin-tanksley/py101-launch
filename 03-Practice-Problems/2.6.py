i = 0
string = ''
while True:
    string += '-'
    i += 1
    if i == 40:
        break

title = "Flintstone Family Members"
prefix_length = (40/2) - (len(title) / 2)
prefix = ""
for i in range(int(prefix_length)):
    prefix += " "
print(prefix+title)
#print(title.center(40))

print(string)

