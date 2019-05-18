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
            print(str(product.id) + '-' + product.name + ': ' + product.descr)
        return self.products

    def add(self, product):

        return self.products.append(product)
