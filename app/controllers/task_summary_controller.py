from flask import Blueprint, jsonify
from app.services.task_service import get_task_summary

summary_bp = Blueprint('summary', __name__)

@summary_bp.route('/', methods=['GET'])
def summary():
    summary_data = get_task_summary()
    return jsonify(summary_data)
