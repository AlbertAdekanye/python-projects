month_conversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "Auguest",
    "Sep": "September",
    "Oct": "October",
    "Nom": "November",
    "Dec": "Devember"
}
#print(month_conversions.get("Mar"))

# loop through the dictionary

for name in month_conversions.keys():
    print(name)