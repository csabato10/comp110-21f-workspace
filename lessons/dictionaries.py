"""Demonstrations of dictionary capabilities."""

# Declaring the type of a dicitonary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key-value pairing in the dictionary
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by it's key -- "lookup"
print(f"UNC has {schools['UNC']} students.")

# Remove a key-value pair from a dictionary
# by it's key
schools.pop("Duke")

# Test for the existence of a key
is_duke_present: bool = "Duke" in schools
print(f"Duke is present: {is_duke_present}")

if "Duke" in schools:
    print("Found the key 'Duke' in schools.")
else:
    print("No key 'Duke' in schools.")

# Update / Reassign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary litereals

# Empty dictionary literal
schools = {}

# Alternatively intialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)