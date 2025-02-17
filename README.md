# Oauth com django

# Registrando um usuário curl -X POST http://127.0.0.1:8000/oauth/register/ -H "Content-Type: application/json" -d '{"username":"daniel", "password":"senha123", "email":"daniel@email.com"}'


# Fazendo login e obtendo o token jwt
curl -X POST http://127.0.0.1:8000/oauth/token/ -H "Content-Type: application/json" -d '{"username":"daniel", "password":"senha123"}'

# Acessando o perfil
curl -X GET http://127.0.0.1:8000/oauth/profile/ -H "Authorization: Bearer SEU_TOKEN"
