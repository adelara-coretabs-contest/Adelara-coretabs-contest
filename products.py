class Products:
    def __init__(self, id, name, cat, descr, photo_url, price):
        self.id = id
        self.name = name
        self.cat = cat
        self.descr = descr
        self.photo_url = photo_url
        self.price = price


class ProductStore:
    def __init__(self, products):
        self.products = products

    def get_all(self):
        for product in self.products:
            print('******************')
            print(str(product.id) + '-' + product.name + '.')
            print('\tPrice: ' + str(product.price) + 'DZD')

            count = 0
            print('\tIngredient: ')
            for ing in product.descr:
                count += 1
                print('\t\t' + str(count) + '- ' + ing)
            print('******************\n')

        return self.products

    def add(self, product):

        return self.products.append(product)
