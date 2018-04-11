#Dictionary Cheatsheet
inventory = {'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
    }
#find some gold
inventory['gold'] += 50
print(inventory["gold"])

#sell dagger
inventory['backpack'].remove("dagger")
inventory['gold'] += 50
#check belongings
print(inventory)
print(inventory["backpack"])


