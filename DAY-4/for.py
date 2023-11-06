users = {'User1': 'Active', 'User2': 'Inactive', 'User3': 'Active'}

# iterate over a copy
for user, status in users.copy().items():
    if status == 'Inactive':
        del users[user]

# Create a new collection
active_user = {}
for user, status in users.items():
    if status == 'Active':
        active_user[user] = status
