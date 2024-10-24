# Creating a set
s = {1, 2, 3}
empty_set = set()  # Empty set

# Unique elements (removes duplicates automatically)
s = {1, 2, 2, 3}
print(f"Set with unique elements: {s}")  # Output: {1, 2, 3}

# Adding elements to the set
s.add(4)
print(f"After adding 4: {s}")

# Removing elements
s.remove(2)
print(f"After removing 2: {s}")

# Discarding (no error if element doesn't exist)
s.discard(5)  # Does nothing, as 5 is not in the set
print(f"After discarding 5: {s}")

# Popping an element (removes and returns an arbitrary element)
popped_element = s.pop()
print(f"Popped element: {popped_element}")
print(f"Set after pop: {s}")

# Clearing the set
s.clear()
print(f"Set after clearing: {s}")

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union
union_set = set1 | set2
print(f"Union of set1 and set2: {union_set}")

# Intersection
intersection_set = set1 & set2
print(f"Intersection of set1 and set2: {intersection_set}")

# Difference
difference_set = set1 - set2
print(f"Difference of set1 and set2: {difference_set}")

# Symmetric Difference
symmetric_diff_set = set1 ^ set2
print(f"Symmetric difference of set1 and set2: {symmetric_diff_set}")

# Set comparisons
set3 = {1, 2}
set4 = {1, 2, 3, 4}
print(f"Is set3 a subset of set4? {set3 <= set4}")
print(f"Is set4 a superset of set3? {set4 >= set3}")

# Set comprehensions
set_comp = {x for x in range(5) if x % 2 == 0}
print(f"Set comprehension result: {set_comp}")

# Length and membership
print(f"Length of set1: {len(set1)}")
print(f"Is 2 in set1? {2 in set1}")

# Copying a set
copied_set = set1.copy()
print(f"Copied set: {copied_set}")

# Frozen set (immutable version of a set)
frozen_set = frozenset([1, 2, 3])
print(f"Frozen set: {frozen_set}")

# Trying to add to frozen set (this will raise an error)
# frozen_set.add(4)  # Uncommenting this will raise an AttributeError
