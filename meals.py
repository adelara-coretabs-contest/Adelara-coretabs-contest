class Meals:
    def __init__(self, id, name, cat, descr, photo_url, price):
        self.id = id
        self.name = name
        self.cat = cat
        self.descr = descr
        self.photo_url = photo_url
        self.price = price


class MealsStore:
    def __init__(self, meals):
        self.meals = meals

    def get_all(self):
        for meal in self.meals:
            print('******************')
            print(str(meal.id) + '-' + meal.name + '.')
            print('\tPrice: ' + str(meal.price) + 'DZD')

            count = 0
            print('\tIngredient: ')
            for ing in meal.descr:
                count += 1
                print('\t\t' + str(count) + '- ' + ing)
            print('******************\n')

        return self.meals

    def get_details(self, id):
        for meal in self.meals:
            if meal.id == id:
                result = meal
                break
            else:
                result = 'Sorry, there\'s no product matching your request!!'
        print(result)
        return result

    def add(self, meal):
        return self.meals.append(meal)

    def remove(self, id):
        meal = self.get_details(id)
        self.meals.remove(meal)
        print(Meals.name + 'is deleted')

