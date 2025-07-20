from flask import jsonify
from datetime import datetime

def success_response(message, data=None):
    """Return a success JSON response."""
    return jsonify({"status": "success", "message": message, "data": data})

def error_response(message, code=400):
    """Return an error JSON response."""
    return jsonify({"status": "error", "message": message}), code

def format_datetime(dt):
    """Format datetime object into a human-readable string."""
    if not dt:
        return None
    return dt.strftime("%Y-%m-%d %H:%M:%S")
