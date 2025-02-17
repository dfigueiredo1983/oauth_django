from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    # Se a exceção for de autenticação, retorna uma mensagem customizada
    if response is not None and response.status_code == 401:
        return Response(
            {
                "detail": "Autenticação falhou. Você precisa fornecer um token JWT válido para acessar esta API.",
                "status_code": 401,
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )

    return response
