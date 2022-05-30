mydict={
    "First Name": "Ananya",
    "Last Name" : "Luthra",
    "Age" : 19,
    "Address" : "Khanna Road, Panipat",
    "State" : "Haryana"
}
print(mydict.items())
print(mydict.keys())
print(mydict.values())
print(type(mydict.items()))
print(list(mydict.keys()))
missing={
    "blood group" : "B+"
}
mydict.update(missing)
print(mydict.items())


