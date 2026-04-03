alien_o = {'x_position': 0, 'y_position': 25, 'speed': 'medium' }
print(f"original position : {alien_o['x_position']}")
if alien_o['speed']=='slow':
    x_increment = 1
elif alien_o['speed'] == 'medium':
    x_increment = 2
elif alien_o['speed'] == 'fast':
    x_increment = 4
else :
    x_increment = 0 
alien_o['x_position'] = alien_o['x_position'] + x_increment
print(f"new position : {alien_o['x_position']}")