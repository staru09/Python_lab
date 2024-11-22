import re

def extract_type(type_string):
    """
    Extracts the type name from a string like "<type 'int'>".
    """
    match = re.search(r"<type '([^']+)'>", type_string)
    if match:
        return match.group(1)  
    return None

print(extract_type("<type 'int'>"))  
print(extract_type("<type 'float'>"))  
print(extract_type("<type 'builtin_function_or_method'>"))  
