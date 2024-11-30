from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class UsuariosView(APIView):
    def get(self, request):
        usuarios = [
            {"nome": "Carlos", "email": "carlos@email.com"},
            {"nome": "João", "email": "joao@email.com"}
        ]
        return Response(usuarios)

class RegisterUserView(APIView):
    def post(self, request):
        data = request.data
        username = data.get('username')
        password = data.get('password')
        email = data.get('email')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return Response({"message": "User created successfully"}, status=status.HTTP_201_CREATED)