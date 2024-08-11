# Initialize the empty dictionary
facilities = {}

# Add some facilities
facilities['Gym'] = {'Location': 'First Floor', 'Open 24/7': True}
facilities['Pool'] = {'Location': 'Ground Floor', 'Open 6 AM to 10 PM': True}
facilities['Library'] = {'Location': 'Second Floor', 'Open 9 AM to 9 PM': True}

# Print the dictionary
print("Facilities:", facilities)

# Access and print information about the Gym
gym_info = facilities.get('Gym')
if gym_info:
    print("Gym Info:", gym_info)
else:
    print("Gym not found")

# Update the Gym's hours
facilities['Gym']['Open 24/7'] = False
print("Updated Gym Info:", facilities['Gym'])

# Remove the Pool from the dictionary
del facilities['Pool']
print("Facilities after removing the Pool:", facilities)
