from app.services.ai_service import analyze_task

def test_ai_service():
    ai_priority, urgency, analysis = analyze_task("Test", "Demo")
    assert ai_priority in ['low', 'medium', 'high', 'urgent']
    assert isinstance(urgency, float)
    assert isinstance(analysis, str)
