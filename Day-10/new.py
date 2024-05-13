player_names=['Shanto','Litton','Riyad','Mushfiq']
print(player_names)

print(player_names[1:3])

#adding something to a list
player_names.append('Sakib')
print(player_names)

#adding something to a list in specific position
player_names.insert(0,'Tamim')
print(player_names)

#removing a value from a list
player_names.remove('Mushfiq')
print(player_names)

#reversing the order of the values in a list
player_names.reverse()
print(player_names)

#removing the last value of a list
player_names.pop()
print(player_names)