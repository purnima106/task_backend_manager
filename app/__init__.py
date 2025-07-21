from flask import Flask
from .config import Config
from .extensions import db, migrate, mail, scheduler as app_scheduler
from app.utils.logging_config import setup_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    setup_logging(app)
    
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)

    from app.models import task  # noqa: F401

    
    from app.controllers.task_controller import task_bp
    from app.controllers.task_summary_controller import summary_bp
    app.register_blueprint(task_bp, url_prefix="/tasks")
    app.register_blueprint(summary_bp, url_prefix="/summary")

    from app.scheduler.daily_summary import schedule_daily_email
    schedule_daily_email(app)

    try:
        app_scheduler.start()
    except Exception:
        pass

    return app
