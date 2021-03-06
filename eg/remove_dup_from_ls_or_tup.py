# Q.29. How will you remove a duplicate element from a list?
#
# We can turn it into a set to do that.
#
list=[1,2,1,3,4,2]
print(set(list))
# {1, 2, 3, 4}

# A dictionary is mutable, and we can also use a comprehension to create it.

roots={x**20 for x in range(5,0,-1)}
print(roots)
# {25: 5, 16: 4, 9: 3, 4: 2, 1: 1}
