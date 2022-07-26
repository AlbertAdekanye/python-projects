# modifying values in a dictionary
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}")

#move the alien to the right
#determine how far to move the alien based on its currents speed

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #this must be the last alien
    x_increment = 3

#the new position is the old position plus the increment
alien_0['x_position'] = alien_0 ['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")