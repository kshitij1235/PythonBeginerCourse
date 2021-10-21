# dictonary


# name : kshitij 
# std  : 5


meridost = {"name":"Rohan","std":5,
            "fav food": "tandoori"
            }

print(meridost)


# printing name
 
print(meridost["name"])
# Rohan

# add


meridost["music"]="hip hop"
print(meridost)
# {'name': 'Rohan', 'std': 5, 'fav food': 'tandoori', 
# 'msic': 'hip hopu'}

# removing a key valuepair 

del meridost["std"]

print(meridost)
# {'name': 'Rohan', 'fav food': 'tandoori', 
# 'music': 'hip hop'}
meridost["std"]="5"
print(meridost)

# {'name': 'Rohan', 'fav food': 'tandoori', 
# 'music': 'hip hop', 'std': '5'}

meridost["std"]="6"
print(meridost)
# {'name': 'Rohan', 'fav food': 'tandoori', 
# 'music': 'hip hop', 'std': '6'}


print(meridost.keys())
# dict_keys(['name', 'fav food', 'music', 'std'])
print(meridost.values())
# dict_values(['Rohan', 'tandoori', 'hip hop', '6'])
