from flask import Flask, render_template, url_for, request, redirect
from meals import Meals, MealsStore
from orders import Orders, OrdersStore
import datetime

app = Flask(__name__)



dummy_meals = [
    Meals(
        1,
        'Pizza',
        1,
        [
            'Tomato sauce',
            'Green olives sliced',
            'Steaks',
            'Cheese Almstazarila'
        ],
        'https://images.pexels.com/photos/1069449/pexels-photo-1069449.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        8
    ),
    Meals(
        2,
        'Hamburger',
        1,
        [
            'Minced meat',
            'Onion slices',
            'Chesar cheese',
            'Sliced Tomatoes',
            'Lettuce',
            'Filled with French fries and Ketchup sauce'
        ],
        'https://images.pexels.com/photos/19642/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        5
    ),
    Meals(
        3,
        'French Burger',
        1,
        [
            'Minced meat',
            'Onion slices ',
            'Sliced tomatoes',
            'Letuce',
            'Pickle',
            'Tahina',
            'Mint'
        ],
        'https://images.pexels.com/photos/47725/hamburger-food-meal-tasty-47725.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        3
    ),
    Meals(
        4,
        'Veg Sandwich',
        1,
        [
            'Toast bread',
            'Chicken breast slices',
            'Letuce',
            'Spices'
        ],
        'https://images.pexels.com/photos/1647163/pexels-photo-1647163.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        6
    ),
    Meals(
        5,
        'Simple Pizza',
        1,
        [
            'Tomatoes sauce',
            'Olive oil',
            'Wild thyme',
            'Mayonnaise'
        ],
        'https://images.pexels.com/photos/1069450/pexels-photo-1069450.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        2
    ),
    Meals(
        6,
        'Sandwich',
        1,
        [
            'Baked bread in medium size',
            'Grilled meat',
            'Colored pepper',
            'Pickle',
            'Mayonnaise'
        ],
        'https://images.pexels.com/photos/1603898/pexels-photo-1603898.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        4
    ),
    Meals(
        7,
        'Leg chicken',
        1,
        [
            'Minced garlic',
            'Fish sauce',
            'Soy sauce',
            'Spicy grated ginger',
            'Hot sauce',
            'Cruched corn flakes'
        ],
        'https://images.pexels.com/photos/60616/fried-chicken-chicken-fried-crunchy-60616.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        5
    ),
    Meals(
        8,
        'Fried meat',
        1,
        [
            'Sheep meat slices',
            'Powder muffins',
            'Curry',
            'Spices of sheep meat',
            'Turmeric'
        ],
        'https://images.pexels.com/photos/991967/pexels-photo-991967.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        9
    )

]

meals = MealsStore(dummy_meals)
meals.get_all()

dummy_orders = []
orders = OrdersStore(dummy_orders)
orders.add(Orders(1, dummy_meals[0], 3, 'Adel', 'my address', 'today'))
orders.get_all()



@app.route('/')
def index():
    title = 'Adelara fast-food chef'
    return render_template('meals.html', admin=False, meals=dummy_meals, title=title)

@app.route('/admin')
def admin_role():
    title = 'Adelara fast-food chef'
    return render_template('meals.html', admin=True, meals=dummy_meals, title=title)



@app.route('/404')
def oops():
    title = "Oops"
    return render_template('404.html' ,title=title)


app.current_id = 1
@app.route('/details/<int:id>', methods=["GET", "POST"])
def details(id):
    meal = meals.get_details(id)
    title = 'Adelara|'+meal.name

    if hasattr(meal, 'id'):
        if request.method == "GET":
            return render_template('details.html', meal=meal, title=title)

        elif request.method == "POST":
            new_order = Orders(id=app.current_id,
                               meal=meal,
                               quantity=int(request.form["quantity"]),
                               user=request.form["user"],
                               address=request.form["address"],
                               date= datetime.datetime.now())
            app.current_id += 1
            orders.add(new_order)
            orders.get_all()
            return redirect(url_for("index"))

    else:
        return redirect(url_for('oops'))

@app.route('/orders')
def list_orders():
    title = 'Adelara|Order'
    return render_template('orders.html', orders=dummy_orders, title=title)

@app.route('/add/meal', methods=["GET", "POST"])
def add_meal():
    title = 'Adelara|Add new meal'
    last_meal_id = dummy_meals[-1].id
    if request.method == "POST":
        last_meal_id += 1
        ings = request.form.getlist("ings[]")
        new_meal = Meals(id=last_meal_id,
                         name=request.form["name"],
                         cat=1,
                         descr=ings,
                         photo_url=request.form["photo"],
                         price=int(request.form["price"])
                         )
        meals.add(new_meal)
        meals.get_all()
        return redirect(url_for("index"))

    elif request.method == "GET":
        return render_template('add-meal.html', title=title)


@app.route('/remove/meal<int:id>')
def meal_remove(id):
    meals.remove(id)
    return redirect(url_for("index"))


@app.route('/update/meal<int:id>', methods=["GET", "POST"])
def meal_update(id):
    if request.method == 'POST':
        ings = request.form.getlist("ings[]")
        update_fields = {
            'name': request.form['name'],
            'cat': int(request.form['cat']),
            'descr': ings,
            'photo_url': request.form['photo'],
            'price': int(request.form['price'])
        }

        meals.update(id, update_fields)

        return redirect(url_for("index"))
    elif request.method == 'GET':
        meal = meals.get_details(id)
        title = 'Adelara|Update '+meal.name
        return render_template('update-meal.html', meal=meal, title=title)