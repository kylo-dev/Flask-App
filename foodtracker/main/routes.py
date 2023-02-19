from flask import Blueprint, render_template, request, redirect, url_for

from foodtracker import db
from foodtracker.models import Food, Log
from datetime import datetime

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    logs = Log.query.order_by(Log.date.desc()).all()

    log_dates = []

    for log in logs:
        proteins = 0
        carbs = 0
        fats = 0
        calories = 0

        for food in log.foods:
            proteins += food.proteins
            carbs += food.carbs
            fats += food.fats
            calories += food.calories

        log_dates.append({
            'log_date': log,
            'proteins': proteins,
            'carbs': carbs,
            'fats': fats,
            'calories': calories
        })
    return render_template('index.html', log_dates=log_dates)

@bp.route('/create_log', methods=['POST'])
def create_log():
    date = request.form['date']
    log = Log(date=datetime.strptime(date, "%Y-%m-%d"))
    db.session.add(log)
    db.session.commit()

    return redirect(url_for('main.view',log_id=log.id))

@bp.route('/add')
def add():
    foods = Food.query.all()
    return render_template('add.html', foods=foods, food=None)

@bp.route('/add', methods=['POST'])
def add_post():
    food_name = request.form['food-name']
    proteins = request.form['protein']
    carbs = request.form['carbohydrates']
    fats = request.form['fat']

    food_id = request.form.get('food-id')
    # food_id가 중복되는 경우 Edit
    if food_id:
        food = Food.query.get_or_404(food_id)
        food.name = food_name
        food.proteins = proteins
        food.carbs = carbs
        food.fats = fats
    # 처음 등록하는 food_id인 경우
    else:
        new_food = Food(
            name=food_name,
            proteins=proteins,
            carbs=carbs,
            fats=fats
        )
        db.session.add(new_food)
    db.session.commit()
    return redirect(url_for('main.add'))   # food 등록 후 'main.add' 페이지 리다이렉트

@bp.route('/delete_food/<int:food_id>')
def delete_food(food_id):
    food = Food.query.get_or_404(food_id)
    db.session.delete(food)
    db.session.commit()

    return redirect(url_for('main.add'))

@bp.route('/edit_food/<int:food_id>')
def edit_food(food_id):
    food = Food.query.get_or_404(food_id)
    foods = Food.query.all()

    return render_template('add.html', food=food, foods=foods)

@bp.route('/view/<int:log_id>')
def view(log_id):
    log = Log.query.get_or_404(log_id)
    foods = Food.query.all()

    totals = {
        'protein' : 0,
        'carbs' : 0,
        'fats' : 0,
        'calories' :0
    }
    for food in log.foods:
        totals['protein'] += food.proteins
        totals['carbs'] += food.carbs
        totals['fats'] += food.fats
        totals['calories'] += food.calories

    return render_template('view.html', foods=foods, log=log, totals=totals)

@bp.route('/add_food_to_log/<int:log_id>', methods=['POST'])
def add_food_to_log(log_id):
    log = Log.query.get_or_404(log_id)
    selected_food = request.form['food-select']

    food = Food.query.get(int(selected_food))

    log.foods.append(food)
    db.session.commit()

    return redirect(url_for('main.view', log_id=log_id))

@bp.route('/remove_food_from_log/<int:log_id>/<int:food_id>')
def remove_food_from_log(log_id, food_id):
    log = Log.query.get_or_404(log_id)
    food = Food.query.get_or_404(food_id)

    log.foods.remove(food)
    db.session.commit()

    return redirect(url_for('main.view', log_id=log_id))