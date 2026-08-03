lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = [i for i in lst1 if isinstance(i, str)]
print(lst2)
