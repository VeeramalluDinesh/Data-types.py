# Creating a dictionary
student = {
    "name": "Dinesh",
    "age": 22,
    "course": "B.Tech",
    "marks": 90
}

print("Original Dictionary:", student)

# Accessing elements
print("Name:", student["name"])
print("Age using get():", student.get("age"))

# Adding new key-value pair
student["college"] = "JNTHU University"
print("After adding college:", student)

# Updating values
student["marks"] = 96
print("After updating marks:", student)

# Removing elements
student.pop("age")   # removes specific key
print("After pop(age):", student)

student.popitem()    # removes last inserted item
print("After popitem():", student)

# Using del
del student["course"]
print("After deleting course:", student)

# Dictionary length
print("Length of dictionary:", len(student))

# Adding multiple items using update()
student.update({"city": "Hyderabad", "grade": "A"})
print("After update():", student)

# Iterating through dictionary
print("\nKeys:")
for key in student.keys():
    print(key)

print("\nValues:")
for value in student.values():
    print(value)

print("\nKey-Value pairs:")
for key, value in student.items():
    print(key, ":", value)

# Copying dictionary
new_student = student.copy()
print("\nCopied Dictionary:", new_student)

# Clearing dictionary
new_student.clear()
print("After clearing copied dictionary:", new_student)

# Creating dictionary using fromkeys()
keys = ("a", "b", "c")
new_dict = dict.fromkeys(keys, 0)
print("Dictionary using fromkeys():", new_dict)
