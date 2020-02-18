def format_price(price):
    numb = int(price)
    phrase = f'Цена: {numb} руб.'
    return phrase

print(format_price(56.24))