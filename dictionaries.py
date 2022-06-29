# my_dict = {'key1': 'Value1', 'key2': 'value2'.......}

bio_mike = {'name': 'Mike', 'age': 45, 'job': 'Engineer', 'location': 'Jos'}
bio_james = {'name': 'James', 'age': 65}

# Accessing the values in a dictionary

# bio_mike['age'] = 50
bio_james['name'] = "James Odoh"

# print(bio_mike["name"], bio_mike['location'], "Boy")

bio_mike['age'] = bio_mike['age'] + 10

# print(bio_mike)

bio_james['gender'] = 'Male'

# print(bio_james)

bio_linda = {'name': 'Linda', 'job': 'Finance officer', 'kin': {'name': "Henry", 'address': {'add1': 'Phase 1 Jalingo', 'add2': 'Phase 2'}}}
print(bio_linda['kin']['address']['add2'])

# Dictionary functions
# .keys()
# print(bio_linda.keys())
# print(bio_linda['kin']['address'].keys())

# .values()
# print(bio_mike.values())

# .items
print(bio_james.items())



