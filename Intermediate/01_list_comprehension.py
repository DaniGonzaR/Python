### List Comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5] 

my_range = range(8)
print(list(my_range))

my_list = [i for i in range(8)] # 0 to 7
print(my_list)
 
my_list = [i + 1 for i in range(8)] # 1 to 8 because i + 1
print(my_list)