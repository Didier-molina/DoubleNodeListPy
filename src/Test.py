from DoubleList import DoubleList

print("test_string")
my_list = DoubleList() 
my_list.add("first")
my_list.add("test")
my_list.add("last")

print(my_list)
print(f"vacío: {my_list.is_empty()}")
deleted = my_list.delete("last")
print(f"borrar: {deleted}")
print(my_list)

print(f"size: {my_list.size()}")
print(f"get(0): {my_list.get(0)}")
print(f"get(size()-1): {my_list.get(my_list.size()-1)}")

deleted = my_list.delete("test")
print(f"borrar: {deleted}")
deleted = my_list.delete("first")
print(f"borrar: {deleted}")
print(f"vacío: {my_list.is_empty()}")
print(my_list)

print("\ntest_int")
my_list_int = DoubleList() 
my_list_int.add(0)
my_list_int.add(1)
my_list_int.add(2)

print(my_list_int)
print(f"vacío: {my_list_int.is_empty()}")
deleted = my_list_int.delete(1)
print(f"borrar: {deleted}")
print(my_list_int)

print(f"size: {my_list_int.size()}")
print(f"get(0): {my_list_int.get(0)}")
print(f"get(size-1): {my_list_int.get(my_list_int.size()-1)}")

deleted = my_list_int.delete(0)
print(f"borrar: {deleted}")
deleted = my_list_int.delete(2)
print(f"borrar: {deleted}")
print(f"vacío: {my_list_int.is_empty()}")
print(my_list_int)