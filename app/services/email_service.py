from flask_mail import Message
from flask import current_app
from app.extensions import mail
from app.services.task_service import get_task_summary

def send_daily_summary_email(recipient_email):
    summary = get_task_summary()

    subject = "Daily Task Summary"
    body = (
        f"Total Tasks: {summary['total_tasks']}\n"
        f"Pending: {summary['pending_tasks']}\n"
        f"Completed: {summary['completed_tasks']}\n"
        f"Overdue: {summary['overdue_tasks']}\n"
        f"Average Urgency: {summary['average_urgency']}"
    )

    msg = Message(subject, sender=current_app.config['MAIL_USERNAME'], recipients=[recipient_email])
    msg.body = body
    mail.send(msg)
    return True
