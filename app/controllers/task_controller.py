from flask import Blueprint, request, jsonify, current_app
from app.services import task_service
from app.extensions import db
from app.services.email_service import send_daily_summary_email

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/', methods=['POST'])
def create_task():
    data = request.get_json()
    task = task_service.create_task(data)
    return jsonify({"message": "Task created", "id": task.id}), 201

@task_bp.route('/', methods=['GET'])
def get_tasks():
    tasks = task_service.get_all_tasks()
    return jsonify([{"id": t.id, "title": t.title, "status": t.status} for t in tasks])

@task_bp.route('/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = task_service.get_task(task_id)
    return jsonify({"id": task.id, "title": task.title, "status": task.status})

@task_bp.route('/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    task = task_service.update_task(task_id, data)
    return jsonify({"message": "Task updated", "id": task.id})

@task_bp.route('/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task_service.delete_task(task_id)
    return jsonify({"message": "Task deleted"})

@task_bp.route('/send-email', methods=['GET'])
def send_email():
    send_daily_summary_email("redmoon210302@gmail.com")
    return {"message": "Email sent"}

@task_bp.route('/log-test', methods=['GET'])
def log_test():
    current_app.logger.info("This is a test log message from /log-test endpoint.")
    return {"message": "Check logs/app.log"}
