# phones = ['iPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8', 'iPhone Xs']

# product = {                                            # также можно писать в одну строку
#     'name': 'iPhone Xs',
#     'stock': 24,
#     'price': 65432.1
# }

# print(product)
# print(len(product))

# product['memory'] = 64
# print(product)

# print(product['stock'])
# print(product.get('name'))
# print(product.get('discount'))
# print(product.get('discount', 0))                  # если ключа нет, но после дописать значение, то вернёт значение по умолчанию. Если ключ есть, то значение по умолчанию игнорируется

# del product['stock']               # если удаляемого ключа нет – ошибка
# print(product)

# product = {                                            
#     'name': 'iPhone Xs',
#     'stock': 24,
#     'price': 65432.1,
#     'recommend': phones
# }

# # print(product)
# print(product['recommend'][1])
# product['recommend'].append('iPhone 6')
# print(product)

# stock = [
#     {'name': 'iPhone Xs Plus', 'stock': 24, 'price': 65432.1, 
#      'recomended': ['Samsung Galaxy S10', 'iPhone Xs']},
#     {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 5000},
#     {'name': 'Xiaomi Mi8', 'stock': 42, 'price': 38000.5}
# ]

# print(type(stock))
# print(type(stock[0]))
# print(stock)
# print(stock[0])
# print(stock[0]['name'])
# stock[0]['price'] = stock[0]['price'] + 10000      # stock[0]['price'] += 10000   same
# print(stock[0])
# print(stock[0]['recomended'][1])

wth = {
    'city': 'Москва',
    'temperature': '20',
}
print(wth)
wth['temperature'] = int(wth['temperature']) - 5
print(wth)

print(wth.get('country'))
wth['country'] = 'Россия'
wth['date'] = '27.05.2019'
print(wth)
print(len(wth))