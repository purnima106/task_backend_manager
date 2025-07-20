from app.extensions import db
from app.models.task import Task
from datetime import datetime
from app.services.ai_service import analyze_task
from sqlalchemy import func

def create_task(data):
    ai_priority, urgency_score, ai_analysis = analyze_task(
        data.get("title"),
        data.get("description"),
        data.get("due_date")
    )
    data["ai_analyzed_priority"] = ai_priority
    data["urgency_score"] = urgency_score
    data["ai_analysis"] = ai_analysis

    task = Task(**data)
    db.session.add(task)
    db.session.commit()
    return task

def get_all_tasks():
    return Task.query.all()

def get_task(task_id):
    return Task.query.get_or_404(task_id)

def get_task_summary():
    total_tasks = Task.query.count()
    pending_tasks = Task.query.filter_by(status='pending').count()
    completed_tasks = Task.query.filter_by(status='completed').count()
    overdue_tasks = Task.query.filter_by(status='overdue').count()

    avg_urgency = db.session.query(func.avg(Task.urgency_score)).scalar() or 0

    return {
        "total_tasks": total_tasks,
        "pending_tasks": pending_tasks,
        "completed_tasks": completed_tasks,
        "overdue_tasks": overdue_tasks,
        "average_urgency": round(avg_urgency, 2)
    }


def update_task(task_id, data):
    task = Task.query.get_or_404(task_id)
    for key, value in data.items():
        setattr(task, key, value)
    task.updated_at = datetime.utcnow()
    db.session.commit()
    return task

def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return task
