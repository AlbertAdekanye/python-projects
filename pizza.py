# store information about a prizza bering orderd.

pizza = {
    "crust": "thick",
    "topping": ["mushrooms", "extra cheese"],
}

# summerize the orderd.

print(f"You orderd a {pizza['crust']}-crust pizza with the following toopings:")
for topping in pizza ["topping"]:
    print("\t" + topping)
