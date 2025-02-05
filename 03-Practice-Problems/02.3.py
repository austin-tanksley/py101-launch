# Programmatically determine whether 42 lies 
# between 10 and 100, inclusive. Do the same 
# for the values 100 and 101.

nums = [42, 100, 101]
for num in nums:
    print(num in range(10,101))

