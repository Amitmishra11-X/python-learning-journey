user = {
    'aeinstein' :{
        'first':'albert',
        'last' : 'einsten',
        'location': 'princeton',
    },
    'mcurie' :{
        'first': 'marie',
        'last' : 'curie',
        'location': 'paris',
    }
}
for usernam, user_info in user.items():
    print(f"\nusername : {usernam.title()}")
    fullname = f"{user_info['first']} {user_info['last']}"
    loc = user_info['location']
    
    print(f"\tFull name : {fullname.title()}")
    print(f"\tLocation : {loc.title()}")