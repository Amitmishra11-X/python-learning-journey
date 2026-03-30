players = ['charles', 'martin', 'michel', 'florene', 'eli']
print(players)
print(players[0:3])
print(players[:3])
print(players[2:])

print(players[-3:])##this prints the names of the last three players 
## Lopping through a slice 
players = ['charles', 'martin', 'michel', 'florene', 'eli']
print("these are my first three players for play:")
for player in players[:3]:
    print(player.title())
