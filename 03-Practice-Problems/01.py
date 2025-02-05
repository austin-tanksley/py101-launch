def ends_with_exclamation(string):
    if len(string) > 0:
        result = string[-1] == "!"
        return  result
    return False

famous_words = "seven years ago..."

print(f"Four score and {famous_words}")

munsters_description = "The Munsters are creepy and spooky."

munsters_description = munsters_description.swapcase()

print(munsters_description)

str1 = "Few things in life are as important as house training your pet dinosaur."
str2 = "Fred and Wilma have a pet dinosaur named Dino."

print("Dino" in str1)
print("Dino" in str2)

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones += ["Dino", "Happy"]

print(flintstones)
advice = "Few things in life are as important as house training your pet dinosaur."
# Expected output:
# Few things in life are as important as
print(advice.split("house"))