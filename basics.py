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

# Also possible to construct list using list comprehension
newList = [x for x in range(1, 11, 1)]
print(newList)


# Tuples - Immutable; only allows methods that do not change tuple structure
print("Tuples and their common methods")
Tuple = (1, 2, 3, 4)

# To print
print(Tuple)

# To print specific index or slice
print(Tuple[-3:])

# To get count of value v
print(Tuple.count(1))

# To get index of first occurrence of value v
print(Tuple.index(1))


# Set - mutable, non-duplicating list, involves hashing and essentially returning 1 value for a key which will store duplicates
print("Sets and their common methods")
# Sets can be created using set(list)
Set = set([1, 2, 3, 4, 4, 4])
print(Set)

# To add elements to a set
Set.add(5)
Set.add(5) # This gets ignored eventually
print(Set)

# To get the difference between Set1 and Set2
Set1 = Set.copy()
Set2 = set([1, 2, 3, 4, 5, 6])
print(Set1.difference(Set2)) # No difference since all elements in Set1 are present in Set2
print(Set2.difference(Set1)) # Extra element in Set2 gets returned

# To get intersection
print(Set1.intersection(Set2))

# To get union
print(Set1.union(Set2))

# To clear out all elements
Set1.clear()
print(Set1)

# To pop first item (NO INDEX CAN BE SPECIFIED)
print(Set2.pop())
print(Set2)