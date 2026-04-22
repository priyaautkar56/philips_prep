import requests

def test_get_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    
    assert response.status_code == 200
    
    data = response.json()
    assert data["id"] == 1
    assert data["username"] == "Bret"
    assert data["email"] == "Sincere@april.biz"


def test_create_user():
    payload = {
        "name": "Priya",
        "username": "priya_test",
        "email": "priya@test.com"
    }
    
    response = requests.post(
        "https://jsonplaceholder.typicode.com/users",
        json=payload
    )
    
    assert response.status_code == 201
    
    data = response.json()
    assert data["name"] == "Priya"
    assert data["email"] == "priya@test.com"
    assert "id" in data    


def test_get_nonexistent_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/999")
    
    assert response.status_code == 404


def test_delete_user():
    response = requests.delete("https://jsonplaceholder.typicode.com/users/1")
    
    assert response.status_code == 200    