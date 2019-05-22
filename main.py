from flask import Flask, render_template, url_for, request, redirect
from meals import Meals, MealsStore
from orders import Orders, OrdersStore

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
        200
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
        140
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
        120
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
                               date='today')
            app.current_id += 1
            orders.add(new_order)
            orders.get_all()
            return redirect(url_for("index"))

    else:
        return redirect(url_for('oops'))
