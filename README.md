# API CRUD Usuários - Prova Técnica PicPay

API RESTful **Flask + SQLite** implementando operações **CRUD** para entidade **Usuário**.

## Endpoints (EXATOS do desafio)

| Método | Endpoint       | Descrição                  |
|--------|----------------|----------------------------|
| `GET`  | `/users`       | Lista todos os usuários    |
| `GET`  | `/users/{id}`  | Detalhes de um usuário     |
| `POST` | `/users`       | Cria novo usuário          |
| `PUT`  | `/users/{id}`  | Atualiza usuário           |
| `DELETE` | `/users/{id}` | Remove usuário             |

## Documentação Interativa (Swagger)
Acesse: **http://localhost:5000/docs/**

## Como Executar

```bash
# 1. Clone
git clone https://github.com/SEU_USUARIO/picpay-flask-crud-users.git
cd picpay-flask-crud-users

# 2. Ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate    # Windows

# 3. Dependências
pip install -r requirements.txt

# 4. Execute
python run.py
```

Acesse: http://localhost:5000/docs/





