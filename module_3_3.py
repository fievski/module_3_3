def print_params(a=1, b='строка', c=True):    # 1. функция с параметрами по умолчанию
    print(a, b, c)

print_params(1, 3, 5)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

def print_params(a, b, c):                     # 2. распаковка параметров
    print(a, b, c)

values_list = [5, 'strong', True]
values_dict = {'a': 1, 'b': False, 'c': 'word'}

print_params(*values_list)
print_params(**values_dict)

def print_params(a, b, c):                     # 3. распаковка + отдельные параметры
    print(a, b, c)
values_list_2 = [25.17, 'текст' ]
print_params(*values_list_2, 52)






# def print_params(a, b, c):
    # print(a, b, c)

# dict_ = {'a': 1, 'b': 2, 'c': 3}
# print_params(**dict_)



# def print_params(a, b, c):
    # print(a, b, c)

# list_ = [1, 2]
# print_params(1, *list_)



# def print_params(*params): #*args **kwargs
    # print(params)

# print_params(1, 2, 3, 4, 5)