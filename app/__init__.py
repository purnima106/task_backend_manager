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

    # --- Import models so metadata loads for Alembic ---
    from app.models import task  # noqa: F401

    # --- Register blueprints ---
    from app.controllers.task_controller import task_bp
    # Change the next line if your file is named differently (task_summary_controller.py)
    from app.controllers.task_summary_controller import summary_bp
    app.register_blueprint(task_bp, url_prefix="/tasks")
    app.register_blueprint(summary_bp, url_prefix="/summary")

    # --- Schedule daily email job BEFORE starting scheduler ---
    from app.scheduler.daily_summary import schedule_daily_email
    schedule_daily_email(app)

    # --- Start scheduler (ignore error if already running) ---
    try:
        app_scheduler.start()
    except Exception:
        pass

    return app
