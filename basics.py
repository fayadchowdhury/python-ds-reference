# Lists - Mutable
print("Lists and their common methods")
List = [1, 2, 3, "GFG", 2.3]

# To append item to a list
List.append("Fayad")

# To extend using an iterable over another iterable structure
List.extend((1, 2, 3))
List.extend([4, 5, 6])

# To insert at index i an element e (can be a list, set, tuple, or other basic data types)
List.insert(3, ["wow", "amaze"])

# To remove the first occurrence of a value v
# Returns ValueError if value v not found
List.remove(1)

# To pop an item at index i (remove and return)
print(List.pop(1))

# To return the count of a value v
print(List.count(2))

# print list
print(List)

# To sort a list of similar data types in ascending order
newList = [4, 3, 5, 2]
newList.sort() # In-place
print(newList)
# Or
newList = [4, 3, 5, 2]
newList = sorted(newList)
print(newList)

# To sort in descending order
newList = [4, 3, 5, 2]
newList.sort(reverse=True)
print(newList)
# Or
newList = [4, 3, 5, 2]
newList = sorted(newList, reverse=True)
print(newList)

# Also possible to sort complex lists using lambda functions as keys
complexList = [
    ("John", "Denver", 42),
    ("John", "Dennings", 56),
    ("Abraham", "Lincoln", 65),
    ("John", "Doe", 24),
]
complexList.sort(key=lambda x: x[2]) # Similar for descending order (reverse=True)
print(complexList)

# To reverse the elements of a list
newList.reverse() # In-place
print(newList)

# To copy a list
newListCopy = newList.copy()
print(newListCopy)

# Without copying, the changes are made in memory addresses and reflected throughout
newListCopy = newList
newListCopy[2] = 5
print(newListCopy)
print(newList)

# To clear a list
newList.clear()
print(newList)