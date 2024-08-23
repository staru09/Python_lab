def merge_lists(list1, list2):
    merged_list = []
    
    len1 = len(list1)
    len2 = len(list2)
    
    for i in range(max(len1, len2)):
        if i < len1:
            l1_elem = list1[i]
        else:
            l1_elem = None
        
        if i < len2:
            l2_elem = list2[-(i + 1)]
        else:
            l2_elem = None
        
        if l1_elem is None:
            merged_list.append(l2_elem if l2_elem is not None else '')
        elif l2_elem is None:
            merged_list.append(l1_elem if l1_elem is not None else '')
        else:
            merged_list.append(l1_elem + l2_elem)
    
    result =  merged_list
    
    return result

list1 = ['A', 'app', 'a', 'd', 'ke', 'th', 'doc', 'awa']
list2 = ['y', 'tor', 'e', 'eps', 'ay', None, 'le', 'n']

result = merge_lists(list1, list2)
print(result)  
