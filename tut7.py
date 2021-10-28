# sets 

set_1 = set([1,2])
set_2 = set([2,3,4,5])

print(type(set_1))
print(set_1)
# {1, 2}

set_1.add(3)
print(set_1)
# {1, 2, 3}    

set_1.add(2)
print(set_1)
# {1, 2, 3}

set_1.add(4)
print(set_1)
# {1, 2, 3, 4}

set_1.remove(4)
print(set_1)
# {1, 2, 3}

print(set_1.union(set_2))
# {1, 2, 3, 4, 5}

print(set_1.intersection(set_2))
# {2, 3}

print(set_1.isdisjoint(set_2))
# False