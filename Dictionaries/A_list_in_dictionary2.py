fav_lang = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'phils' : ['python', 'haskell'],
}
for name, languages in fav_lang.items():
    print(f"\n{name.title()}'s favorite language are : ")
    for language in languages:
        print(f"\n{language.title()}")