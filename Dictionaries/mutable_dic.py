alien_o = {'color' : 'green'}
print(f"the alein is{alien_o['color']}")

alien_o['color'] = 'yellow'
print(f"the alein is{alien_o['color']}")
# modifying values in a dictionary

alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print(f"original position of x : {alien_o['x_position']}")
if alien_o['speed']=='slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
elif alien_o['speed'] == 'fast':
    x_increment = 4
else :
    x_increment = 0 
alien_o['x_position'] = alien_o['x_position'] + x_increment
print(f"new position of x: {alien_o['x_position']}")