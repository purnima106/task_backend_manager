import random
from datetime import datetime

# Mock AI analysis for now
def analyze_task(title, description, due_date=None):
    # Priority logic (mocked)
    priority_levels = ['low', 'medium', 'high', 'urgent']
    ai_priority = random.choice(priority_levels)

    # Urgency score
    urgency_score = random.uniform(0, 1)
    if due_date and isinstance(due_date, datetime):
        days_left = (due_date - datetime.utcnow()).days
        if days_left <= 2:
            urgency_score = min(1.0, urgency_score + 0.4)

    ai_analysis = f"AI suggests priority '{ai_priority}' with urgency score {urgency_score:.2f}."
    return ai_priority, urgency_score, ai_analysis
