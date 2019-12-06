from acme import Product
from random import choice, randint

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(quant_prods=30):
    products_list = []

    for x in range(0, quant_prods):
        t = Product(input_name=(choice(ADJECTIVES)+' '+choice(NOUNS)))
        t.price = randint(5, 100)
        t.weight = randint(5, 100)
        t.flammability = float(randint(0, 25)) / 10
        products_list.append(t)

    return products_list


def inventory_report(product_list):
    unique_names = []
    prices = []
    weights = []
    flams = []

    for item in product_list:
        if(item.name not in unique_names):
            unique_names.append(item.name)
        prices.append(item.price)
        weights.append(item.weight)
        flams.append(item.flammability)

    # E501 for pycodestyle: Unable to shorten length as it is a single variable
    str = 'Unique Names:\t{}\nMean Price:\t{}\nMean Weight:\t{}\nMean Flamabiltiy:\t{}'

    formatted_str = str.format(len(unique_names),
                               sum(prices)/len(product_list),
                               sum(weights)/len(product_list),
                               sum(flams)/len(product_list))

    print(formatted_str)
    return formatted_str


if __name__ == '__main__':
    inventory_report(generate_products())
