def test_create_task(client):
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Demo"})
    assert response.status_code == 201
    assert response.get_json()["message"] == "Task created"

def test_get_tasks(client):
    # Create a task first
    client.post("/tasks/", json={"title": "Task 1"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
