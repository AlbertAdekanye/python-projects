"""def get_formatted_name(first_name, middle_name, last_name):
    #Return a fullname, neatly formatted
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
best_pal = get_formatted_name("alaofin", "tomi", "marvellous")
print(best_pal)"""

#making midddle_name optional
def get_formatted_name(first_name, last_name, middle_name=""):
   if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
   else:
        full_name = f"{first_name} {last_name}"
   return full_name.title()
best_pal = get_formatted_name("alaofin", "marvellous")
print(best_pal)
best_pal = get_formatted_name("alaofin", "marvellous", "tomi")
print(best_pal)





