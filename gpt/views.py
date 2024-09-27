from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import UsernameSerializer
from .gpt import generate_message, parse_instagram


class UsernameView(generics.GenericAPIView):
    serializer_class = UsernameSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_data = parse_instagram(request.data['username'])
        message = generate_message(user_data['bio'], user_data['posts_title'])
        return Response({'message': message}, status=status.HTTP_200_OK)

