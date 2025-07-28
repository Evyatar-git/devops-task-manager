from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Task

# Blueprint = a way to organize related routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home page - shows all tasks"""
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['GET', 'POST'])
def add_task():
    """Add a new task"""
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        
        if title:
            task = Task(title=title, description=description)
            db.session.add(task)
            db.session.commit()
            flash('Task added successfully!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Title is required!', 'error')
    
    return render_template('add_task.html')

@main.route('/complete/<int:task_id>')
def complete_task(task_id):
    """Mark a task as completed"""
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    flash('Task completed!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    """Delete a task"""
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'success')
    return redirect(url_for('main.index'))

# API endpoint for health checks (important for monitoring later)
@main.route('/health')
def health_check():
    """Simple health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Task Manager is running'})