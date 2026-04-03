user_1 = {
    'username':'smishra',
    'first':'suraj',
    'last' :'mishra'
    
}
for key, value in user_1.items():
    print(f"KEY: {key}")
    print(f"VALUE:{value}")

favorite_languages = {
    'devang':'python',
    'suraj':'java',
    'adarsh':'c++',
    'adesh':'c'
}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}")
for name in favorite_languages.keys():
    print(name.title())
