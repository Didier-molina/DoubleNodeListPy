from DoubleList import DoubleList

my_list = DoubleList() 
my_list.add("first")
my_list.add("test")
my_list.add("test")
my_list.add("test")
my_list.add("test")
my_list.add("last")

print(my_list)
print(my_list.size())
print(my_list.get(0))
print(my_list.get(my_list.size()-1))