# Declare a dict
name_to_age_map = {}

# Set it's keys followed by values.
name_to_age_map["Ann"] = 16
name_to_age_map["Bob"] = 12
name_to_age_map["Sam"] = 14

# .keys() returns a list of all keys in the dictionary
print(name_to_age_map.keys())

# .values() returns a list of all values in the dictionary
print(name_to_age_map.values())

# .items() returns a list of tuples with all key value pairs in the dictionary
print(name_to_age_map.items())

# We can check if a key is in the dictionary with O(1) time.
print("Ryan" in name_to_age_map)
print("Sam" in name_to_age_map)

# We can check value of specific key in O(1) time
print(name_to_age_map.get("Ryan"))
print(name_to_age_map.get("Sam"))

# Directly accessing a key that doesn't exist will result in an error.
# If you don't comment this out python will error out
# name_to_age_map["Ryan"]
name_to_age_map["Sam"]

# Careful not to do the following as it's O(n) runtime! This will check all
# items in a list not a dictionary
"Sam" in name_to_age_map.keys()





