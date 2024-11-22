def get_value(data_list, index):
    try:
        return data_list[index] 
    except IndexError:
        return None 
my_list = ['a', 'b', 'c']

print(get_value(my_list, 1))  
print(get_value(my_list, 5))  
