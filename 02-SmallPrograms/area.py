import pdb

def invalid_input(input):
    try:
        float(input)
    except ValueError:
        return True
    
    return False
        


length = input("==> What is the length of the room in meters? \n")
while invalid_input(length):
    length = input("==> Input invalid. Please enter a valid number \n")

width = input("==> What is the width of the room in meters? \n")
while invalid_input(length):
    width = input("==> Input invalid. Please enter a valid number \n")


def get_area(length,width, unit="meters"):
    
    unit = unit.lower()
    if unit == "feet":
        return length * width * 10.7639
    
    return length * width

print(f"{get_area(float(length), float(width))} sqmt")
print(f"{get_area(float(length), float(width), 'feet')} sqft")
