# Рекурсивная версия
def find_recursive(obj, value):
    def flatten(lst):
        result = []
        for item in lst:
            if isinstance(item, list):
                result.extend(flatten(item))
            else:
                result.append(item)
        return result
    flat = flatten(obj)
    try:
        return flat.index(value)
    except ValueError:
        return None

# Итеративная версия 
def find_iterative(obj, value):
    flat = []
    stack = [obj]
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            
            for item in reversed(current):
                stack.append(item)
        else:
            flat.append(current)
    
    try:
        return flat.index(value)
    except ValueError:
        return None


print(find_recursive([1, 2, [3, 4, [5, [6, [[]]]]], 4], 4))   
print(find_recursive([1, 2, [3, 4, [5, [6, [[]]]]], 'spam'], 'spam'))  
print(find_iterative([1, 2, [3, 4, [5, [6, [[]]]]], 4], 4))   
print(find_iterative([1, 2, [3, 4, [5, [6, [[]]]]], 'spam'], 'spam'))  
