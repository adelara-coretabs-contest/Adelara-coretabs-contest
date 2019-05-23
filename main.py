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
            'Fromage',
            'Thon',
            'Olive',
        ],
        'https://images.pexels.com/photos/724216/pexels-photo-724216.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        8
    ),
    Meals(
        2,
        'Sandwich',
        1,
        [
            'Fromage',
            'Viande Hachée',
            'Frittes',
            'Omelette',
            'Salade'
        ],
        'https://images.pexels.com/photos/357746/pexels-photo-357746.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        5
    ),
    Meals(
        3,
        'Hamburger',
        1,
        [
            'Fromage',
            'Viande Hachée',
            'Frittes',
            'Omelette',
            'Salade'
        ],
        'https://images.pexels.com/photos/1639562/pexels-photo-1639562.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=940',
        3
    ),
]

meals = MealsStore(dummy_meals)
meals.get_all()

dummy_orders = []
orders = OrdersStore(dummy_orders)
orders.add(Orders(1, dummy_meals[0], 3, 'Adel', 'my address', 'today'))
orders.get_all()



@app.route('/')
def index():
    return render_template('index.html', meals=dummy_meals)

@app.route('/404')
def oops():
    return render_template('404.html')


app.current_id = 1
@app.route('/details/<int:id>', methods=["GET", "POST"])
def details(id):
    meal = meals.get_details(id)

    if hasattr(meal, 'id'):
        if request.method == "GET":
            return render_template('details.html', meal=meal)

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
    return render_template('orders.html', orders=dummy_orders)

@app.route('/add/meal', methods=["GET", "POST"])
def add_meal():
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
        return render_template('add-meal.html')


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
        return render_template('update-meal.html', meal=meal)