class Orders:
    def __init__(self, id, meal, quantity, user, date):
        self.id = id
        self.meal = meal.id
        self.quantity = quantity
        self.user = user
        self.date = date
        self.amount = meal.price * quantity



class OrdersStore:
    def __init__(self, orders):
        self.orders = orders

    def get_all(self):
        for order in self.orders:
            print('******************')
            print(str(order.id) + '-' + order.user + '.')
            print('\tQuantity: ' + str(order.quantity))
            print('\tAmount: $' + str(order.amount))
        return self.orders

    def get_order(self, id):
        for order in self.order:
            if order.id == id:
                result = order
                break
            else:
                result = 'Sorry, there\'s no order matching your request!!'
        print(result)
        return result

    def add(self, order):
        return self.orders.append(order)
