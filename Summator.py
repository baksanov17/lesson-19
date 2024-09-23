def summator(data_structure):
    counter = 0
    if isinstance(data_structure, (list, tuple, set)):
        for i in data_structure:
            counter += summator(i)
    elif isinstance(data_structure, dict):
        for key, value in data_structure.items():
            counter += summator(key)
            counter += summator(value)
    elif isinstance(data_structure, str):
        counter += len(data_structure)
    elif isinstance(data_structure, (int, float)):
        counter += data_structure
    return counter


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = summator(data_structure)
print(result)
