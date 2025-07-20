# app/scheduler/daily_summary.py
from app.extensions import scheduler
from app.services.email_service import send_daily_summary_email

def schedule_daily_email(app, recipient="your_email@gmail.com"):
    """Register a 9:00 AM daily email job with APScheduler."""
    try:
        scheduler.remove_job('daily_email_job')
    except Exception:
        pass

    def _send():
        with app.app_context():
            send_daily_summary_email(recipient)

    scheduler.add_job(_send, 'cron', hour=9, minute=0, id='daily_email_job')
