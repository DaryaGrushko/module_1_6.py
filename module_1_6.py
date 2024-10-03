#Практическое задание по теме: "Словари и множества"

print ('---------- 1 часть - словари---------------')
my_dict = {'Irina' : 1995, 'Sasha' : 2000, 'Marina' : 1990, 'Glafira' : 2015}
print('Словарь:', my_dict)
print('Значение словаря по существующему ключу "Glafira" = ', my_dict['Glafira'])
print('Значение словаря по несуществующему ключу "Gla" = ', my_dict.get('Gla'))
my_dict.update({'Katya':2011,
                 'Roman':2022,})
print('Словарь с добавленными значениями:', my_dict)
dell = my_dict.pop('Irina')
print('Значение удаленного элемента "Irina" :', dell)
print('Словарь после удасления элемента:', my_dict)

print ('\n---------- 2 часть - множества---------------')
my_set = {33, 77, 88,True, (9,8,1), 33, True, 'Tanya'}
print('Множество : ', my_set)
my_set.update([5], ['Vasya'])
print('Множество после добавления 2 значений "[5], [Vasya]": ', my_set)
my_set.remove(77)
print('Множество после удаления 1 значения "77": ', my_set)