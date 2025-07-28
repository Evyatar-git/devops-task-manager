from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from app import db
from app.models import Task

main = Blueprint('main', __name__)

@main.route('/')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@main.route('/add', methods=['GET', 'POST'])
def add_task():
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
    task = Task.query.get_or_404(task_id)
    task.completed = True
    db.session.commit()
    flash('Task completed!', 'success')
    return redirect(url_for('main.index'))

@main.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    flash('Task deleted!', 'success')
    return redirect(url_for('main.index'))

@main.route('/health')
def health_check():
    """Simple health check that doesn't require database"""
    return {'status': 'healthy', 'message': 'Task Manager is running'}

@main.route('/health/detailed')
def detailed_health_check():
    """Detailed health check that tests database connectivity"""
    try:
        # Test database connection
        task_count = Task.query.count()
        return jsonify({
            'status': 'healthy', 
            'message': 'Task Manager is running',
            'database': 'connected',
            'task_count': task_count
        })
    except Exception as e:
        return jsonify({
            'status': 'unhealthy',
            'message': str(e),
            'database': 'disconnected'
        }), 500