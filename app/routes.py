from app import app
from flask import render_template
import flag

@app.route('/')
def index():
    return render_template('index.html', name='Luis')

@app.route('/favorite')
def favorite():
    favorite_players = [
        ('1. Lionel Messi',flag.flag('AR')),
        ('2. Ronaldinho Gaucho', flag.flag('BR')), 
        ('3. Ronaldo Nazario', flag.flag('BR')), 
        ('4. Diego Maradona', flag.flag('AR')), 
        ('5. Zinedine Zidane', flag.flag('FR'))
    ]
    return render_template('favorites.html', name='Luis', players=favorite_players)