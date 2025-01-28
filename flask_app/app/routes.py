from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Task
from app import db

task_routes = Blueprint('task_routes', __name__)

@task_routes.route('/create_task', methods=['GET', 'POST'])
@login_required
def create_task():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        task = Task(title=title, description=description, user_id=current_user.id)
        db.session.add(task)
        db.session.commit()
        flash('Task created successfully!')
        return redirect(url_for('task_routes.dashboard'))
    return render_template('create_task.html')

@task_routes.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('You do not have permission to edit this task.')
        return redirect(url_for('task_routes.dashboard'))

    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        db.session.commit()
        flash('Task updated successfully!')
        return redirect(url_for('task_routes.dashboard'))
    return render_template('edit_task.html', task=task)

@task_routes.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id != current_user.id:
        flash('You do not have permission to delete this task.')
        return redirect(url_for('task_routes.dashboard'))

    db.session.delete(task)
    db.session.commit()
    flash('Task deleted successfully!')
    return redirect(url_for('task_routes.dashboard'))