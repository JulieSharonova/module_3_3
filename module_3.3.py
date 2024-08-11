#1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params()
print_params(6, 'happy')
print_params(10, 'none', False)
print_params(120)
print_params(44, 2, 77)

print_params(b = 25)
print_params(c = [1, 2, 3])

# 2.Распаковка параметров:
value_list = [1, 'life', False]
value_dict = {'a' : 4, 'b' : 'world','c' : True}
print_params(*value_list)                           # Передайте values_list и values_dict в функцию print_params, используя распаковку параметров
print_params(**value_dict)                          # (* для списка и ** для словаря).

# 3.Распаковка + отдельные параметры:
value_list_2 = [5, 'week']
print_params(*value_list_2, 42)
# Создайте список values_list_2 с двумя элементами разных типов
# Проверьте, работает ли print_params(*values_list_2, 42)
