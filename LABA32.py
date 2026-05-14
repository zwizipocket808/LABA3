# Рекурсивная версия
def recurrence_recursive(u, v, n):
    if n == 1:
        return u, v
    a_prev, b_prev = recurrence_recursive(u, v, n-1)
    a = 2 * b_prev + a_prev
    b = 2 * b_prev * b_prev + b_prev   # b_prev^2
    return a, b

# Итеративная версия
def recurrence_iterative(u, v, n):
    a, b = u, v
    for _ in range(2, n+1):
        a, b = 2 * b + a, 2 * b * b + b
    return a, b


u, v, n = 1, 2, 3
print(recurrence_recursive(u, v, n))   
 
