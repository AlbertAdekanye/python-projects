favorite_languages = {
    "albert": ["python", "c++"],
    "prazi": ["c"],
    "justin": ["java-script", "flutter"],
    "austin": ["java", "c#"],
}

for names, languages in favorite_languages.items():
    print(f"\n{names.title()}'s favorite_languages are: ")
    for language in languages:
        print(f"\t {language.title()}")