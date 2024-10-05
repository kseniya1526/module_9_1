def apply_all_func(int_list, *functions):
    result = {}
    for new_func in functions:
        try:
            result[new_func.__name__] = new_func(int_list)
        except Exception as exc:
            result[new_func.__name__] = f'Ошибка: {str(exc)}'
    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))