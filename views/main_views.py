from flask import Blueprint, render_template, request, redirect, url_for
from todo.models import Todo
from todo import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    # show all todos
    todo_list = Todo.query.all()
    return render_template('base.html', todo_list=todo_list)

@bp.route('/add', methods=["POST"])
def add():
    # add new item
    title = request.form.get('title')
    new_todo = Todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/update/<int:todo_id>') # /update/<int:todo_id> : 실행시 볼 수 없는 URI에서 코드 실행 후 반환
def update(todo_id):
    # update item
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('main.index'))

@bp.route('/delete/<int:todo_id>')
def delete(todo_id):
    # delete item
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('main.index'))