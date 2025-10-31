# Criar usuário (POST /users)
curl -X POST http://localhost:5000/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Ana", "email": "ana@picpay.com"}'

# Listar todos (GET /users)
curl http://localhost:5000/users

# Detalhes (GET /users/{id})
curl -X GET http://localhost:5000/users/1

# Atualizar (PUT /users/{id})
curl -X PUT http://localhost:5000/users/1 \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Ana Costa Silva",
    "email": "ana.silva@picpay.com"
  }'

# Deletar (DELETE /users/{id})
curl -X DELETE http://localhost:5000/users/1