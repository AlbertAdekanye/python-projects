users = {
    "jae" : {
        "first" : "johnpeace",
        "last" : "oyebade",
        "location" : "omu_aran",
    },

    "alberto" : {
        "first" : "albert",
        "last" : "adekanye",
        "location" : "omu_aran",
    },
}
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")