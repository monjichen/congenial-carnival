# NON-INTERACTIVE CODE CELL. YOU MAY RUN THIS CELL, BUT DO NOT EDIT IT.
# FOR DEMONSTRATION PURPOSES ONLY. DO NOT EDIT.

products = {
    "americano":{"name":"Americano","price":150.00},
    "brewedcoffee":{"name":"Brewed Coffee","price":110.00},
    "cappuccino":{"name":"Cappuccino","price":170.00},
    "dalgona":{"name":"Dalgona","price":170.00},
    "espresso":{"name":"Espresso","price":140.00},
    "frappuccino":{"name":"Frappuccino","price":170.00},
}

# CODE CELL
# PROBLEM 1
def get_product(code):
    return products[code]

get_product('frappuccino')

# CODE CELL
# PROBLEM 2

def get_property(code, property):
    return products[code][property]
    
get_property('frappuccino', 'price')

# CODE CELL
# PROBLEM 3

def main():
    
    americano = 0
    brewedcoffee = 0
    cappuccino = 0
    dalgona = 0
    espresso = 0
    frappuccino = 0
    total = 0

    while True:
        order = input('Input your order using the format "product_code, quantity" then input "/" to proceed to checkout: ')
        if order == '/':
            break
        else:
            product_code, quantity = order.split(',')
            
            if product_code == 'americano':
                americano += int(quantity)
            elif product_code == 'brewedcoffee':
                brewedcoffee += int(quantity)
            elif product_code == 'cappuccino':
                cappuccino += int(quantity)
            elif product_code == 'dalgona':
                dalgona += int(quantity)
            elif product_code == 'espresso':
                espresso += int(quantity)
            elif product_code == 'frappuccino':
                frappuccino += int(quantity)
            else:
                pass

            total += get_property(product_code, 'price') * int(quantity)

    receipt = []
            
    if americano > 0:
        receipt += [('americano', americano)]
    if brewedcoffee > 0:
        receipt += [('brewedcoffee', brewedcoffee)]
    if cappuccino > 0:
        receipt += [('cappuccino', cappuccino)]
    if dalgona > 0:
        receipt += [('dalgona', dalgona)]
    if espresso > 0:
        receipt += [('espresso', espresso)]
    if frappuccino > 0:
        receipt += [('frappuccino', frappuccino)]

    with open('receipt.txt', 'w') as f:
        f.write('''
==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL
''')

    for items in receipt:
        code = items[0]
        name = get_property(code, 'name')
        quantity = items[1]
        subtotal = get_property(code, 'price') * int(quantity)

        with open('receipt.txt', 'a') as f:
            if code == 'dalgona':
                f.write(f'\n{code}\t\t\t{name}\t\t\t{quantity}\t\t\t\t{subtotal}')
            else:
                f.write(f'\n{code}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}')

    with open('receipt.txt', 'a+') as f:
        f.write(f'''\n
Total:\t\t\t\t\t\t\t\t\t\t{total}
==
''')
        f.seek(0)
        print(f.read())

main()