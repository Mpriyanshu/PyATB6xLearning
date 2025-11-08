from src.ex_13_List.Lab96_List import my_list

squares = {x**2 for x in range(5)}
print(squares)

# frozen set (Immutable set)
# A frozenset cannot be changed after creation

my_list = [1, 2, 3,3]
fset = frozenset(my_list)
print(fset)
#fset.add(4) # AttributeError: 'frozenset' object has no attribute 'add'
