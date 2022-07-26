favorite_number = {
    "Albert": 7,
    "John": 10,
    "James": 14,
    "tony": 8,
    "Adesoye": 11,
}
#number = favorite_number ["Albert"]
#print(f"Albert's favorite_number is {number}")

#looping through the dictionary 
for name, number in favorite_number.items():
    print(f"{name}'s favorite_number is {number}.")
    
# printing only the names through loop
for name in favorite_number.keys():
    print(name)