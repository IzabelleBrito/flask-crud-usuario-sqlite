# === TESTES DE CRIAÇÃO ===
def test_create_user_success(client):
    response = client.post('/users', json={
        'name': 'João Silva',
        'email': 'joao@picpay.com',
        'password': '123456'
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'João Silva'
    assert data['email'] == 'joao@picpay.com'
    assert 'id' in data

def test_create_user_short_password(client):
    response = client.post('/users', json={
        'name': 'Maria', 'email': 'maria@picpay.com', 'password': '123'
    })
    assert response.status_code == 400
    assert 'Senha' in response.get_json()['error']

def test_create_user_invalid_email(client):
    response = client.post('/users', json={
        'name': 'Pedro', 'email': 'invalid', 'password': '123456'
    })
    assert response.status_code == 400
    assert 'Email' in response.get_json()['error']

def test_create_user_duplicate_email(client):
    # Primeiro
    client.post('/users', json={
        'name': 'Ana', 'email': 'ana@picpay.com', 'password': '123456'
    })
    # Segundo (mesmo email)
    response = client.post('/users', json={
        'name': 'Ana 2', 'email': 'ana@picpay.com', 'password': '123456'
    })
    assert response.status_code == 400
    assert 'Email já cadastrado' in response.get_json()['error']

# === LISTAGEM ===
def test_get_all_users(client):
    client.post('/users', json={
        'name': 'Lucas', 'email': 'lucas@picpay.com', 'password': '123456'
    })
    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) >= 1
    assert any(u['email'] == 'lucas@picpay.com' for u in data)

# === DETALHE ===
def test_get_user_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == 404

# === ATUALIZAÇÃO ===
def test_update_user(client):
    create = client.post('/users', json={
        'name': 'Carlos', 'email': 'carlos@picpay.com', 'password': '123456'
    })
    user_id = create.get_json()['id']

    update = client.put(f'/users/{user_id}', json={
        'name': 'Carlos Silva',
        'email': 'carlos.silva@picpay.com'
    })
    assert update.status_code == 200
    data = update.get_json()
    assert data['name'] == 'Carlos Silva'
    assert data['email'] == 'carlos.silva@picpay.com'

# === EXCLUSÃO ===
def test_delete_user(client):
    create = client.post('/users', json={
        'name': 'Beatriz', 'email': 'beatriz@picpay.com', 'password': '123456'
    })
    user_id = create.get_json()['id']

    delete = client.delete(f'/users/{user_id}')
    assert delete.status_code == 204

    get = client.get(f'/users/{user_id}')
    assert get.status_code == 404