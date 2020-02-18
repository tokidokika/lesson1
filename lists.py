# phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8', 'iPhone Xs']   # переменные живут ровно до тех пор, пока работает программа

# print(phones)

# phones_count = len(phones)
# print(phones_count)

# phones.append('iPhone Xs')   # кладёт элемент в конец списка
# print(phones)

# print(phones.count('iPhone Xs'))
# print(phones.count('iPhone 9'))
  
# print(phones[1])  # обращение по индексу. Если выйти за границы списка по индексу, то выдаст ошибку

# print(phones[1:3])
# print(phones[:2])
# print(phones[-1])

# print(phones.index('Xiaomi Mi8'))
# phones.sort()           # если в списке разные типы данных, то сортировка не сработает и надо будет писать свой собственный сортировщик
# print(phones.sort())  # не работает?
# print(phones)

# print('iPhone Xs' in phones)   #проверка элменета на вхождение в список (регистр букв важен)
# print('iPhone X' in phones)

# print(phones)
# # del phones[3]
# # print(phones)
# phones.remove('Samsung Galaxy S10')    # удаляет первый попавшийся совпадающий элемент. Если таких элементов несколько, нужно использовать ремув столько раз, сколько нужно удалить элементы
# print(phones)   


numbers = [3, 5, 7, 9, 10.5]
numbers.append('Python')
print(len(numbers))
print(numbers[:1])
print(numbers[-1])
print(numbers[2:5])
numbers.remove('Python')
print(numbers)