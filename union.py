set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

# Using the | operator
union_set = set1 | set2
print(union_set)

# Using the union() method
union_set = set1.union(set2)
print(union_set)

set1 = {'a', 'e', 'i', 'o', 'u', 'y'}
set2 = {'a', 'e', 'i', 'o', 'u', 'y', 'æ', 'ø', 'å'}

# Union
union = set1.union(set2)
print("Union:", union)

# Symmetric Difference
sym_diff = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff)

# Difference
diff1 = set1.difference(set2)
print("Difference of set1 from set2:", diff1)

diff2 = set2.difference(set1)
print("Difference of set2 from set1:", diff2)

# Disjoint
disjoint = set1.isdisjoint(set2)
print("Are the sets disjoint?", disjoint)

#datastructure
data = {'a': 'Alpha', 'b': 'Beta', 'g': 'Gamma'}

# create a list of tuples using a list comprehension
result = [(key, value) for key, value in data.items()]

print(result)