# price = 100
# discount = 5
# price_with_discount = price - price * discount / 100

# print(price_with_discount)


# def discounted(price, discount):
#     price_with_discount = price - (price * discount / 100)
#     print(price_with_discount)

# discounted(100, 6)
# discounted(200, 20)
# discounted(1500, 9)


# def discounted(price, discount):
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     print(price_with_discount)

# discounted(100, 101)


# def discounted(price, discount):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     print(price_with_discount)

# discounted(150, 20)
# discounted(250, -20)
# discounted(-3040, 20)


# def discounted(price, discount):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     if discount >= 100:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     return(price_with_discount)

# product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 50}
# product['with_discount'] = discounted(product['price'], product['discount'])
# print(product)

# def discounted(price, discount, max_discount=50):
#     price = abs(float(price))
#     discount = abs(float(discount))
#     max_discount = abs(float(max_discount))
#     if max_discount > 99:
#         raise ValueError('Максимальная скидка не может быть больше 99%')
#     if discount >= max_discount:
#         price_with_discount = price
#     else:
#         price_with_discount = price - (price * discount / 100)
#     return price_with_discount

# # product = {'name': 'Samsung Galaxy S10', 'stock': 8, 'price': 50000.0, 'discount': 70}
# # product['with_discount'] = discounted(product['price'], product['discount'], max_discount=80)
# # print(product)
# # discounted(100, 50, max_discount=100)
# print(discounted(100, 40))





# def get_summ(one, two, delimmiter='&'):
#     parametr1 = str(one)
#     parametr2 = str(two)
#     answer = parametr1 + delimmiter + parametr2
#     return answer

# parameters = get_summ('лог', 'дом')
# print(parameters)


# def words(word1, word2):
#     pon = str(word1)
#     pon2 = str(word2)
#     ponk = pon + ' ' + pon2
#     return ponk

# ponc = words('Learn', 'python')
# print(ponc)
# print(ponc.upper())