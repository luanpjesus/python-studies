import requests

# CRUD
BASE_URL = "http://127.0.0.1:5000"
tasks = []


def test_create_task():
    new_tesk_data = {"title": "Nova tarefa", "description": "Descricao da nova tarefa"}
    response = requests.post(f"{BASE_URL}/tasks", json=new_tesk_data)
    assert response.status_code == 200
    response_json = response.json()
    assert "message" in response_json
    assert "id" in response_json

    tasks.append(response_json["id"])


def test_get_tasks():
    response = requests.get(
        f"{BASE_URL}/tasks",
    )
    # No caso do get nao precisa para o json, pq nao tem post so vai pegar os dados
    assert response.status_code == 200
    # Esse me todo recupera e salva o json da request na variavel
    response_json = response.json()
    print(response_json)
    assert "task" in response_json
    assert "total_tasks" in response_json


def test_get_task():
    if tasks:
        task_id = tasks[0]
        response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200
        response_json = response.json()
        assert task_id == response_json["id"]


def test_update_task():
    if tasks:
        task_id = tasks[0]
        payload = {
            "title": "Titulo atualizado",
            "completed": False,
            "description": "Nova descricao",
        }

        response = requests.put(f"{BASE_URL}/tasks/{task_id}", json=payload)

        assert response.status_code == 200
        response_json = response.json()
        assert "message" in response_json

        get_response = requests.get(f"{BASE_URL}/tasks/{task_id}")
        assert get_response.status_code == 200

        task = get_response.json()
        assert task["title"] == payload["title"]
        assert task["description"] == payload["description"]
        assert task["completed"] == payload["completed"]


def test_delete_task():
    if tasks:
        task_id = tasks[0]
        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 200

        response = requests.delete(f"{BASE_URL}/tasks/{task_id}")
        assert response.status_code == 404
