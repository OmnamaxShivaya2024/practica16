def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(8)
print_params(5, 6)
print_params(9, 5, 2)
print_params()
print_params("------------------------")

print_params(b=25)
print_params(c=[1,2,3])
print_params("------------------------")

values_list = [4, True, "dog"]
values_dict= {"a": 54, "b":False, "c": "cat"}
print_params(*values_list)
print_params(**values_dict)
print("--------------")

values_list_2=[1.5,(32,5)]
print_params(*values_list_2,42)


