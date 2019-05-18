from flask import Flask, render_template
from products import Products, ProductStore

app = Flask(__name__)

dummy_products = [
    Products(
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
    Products(
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
    Products(
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

@app.route('/')
def index():
    return render_template('index.html', hello='Hello Adelara clients')