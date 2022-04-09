from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import User
from .serializers import RegisterSerializer, UserSerializer, PswdChangeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, logout
from rest_framework.decorators import  api_view, permission_classes
from rest_framework.response import Response
from django.utils.translation import gettext_lazy as _
from config.permissions import IsProfileOwner
from rest_framework import status

class UserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class UserRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsProfileOwner)

    def get_serializer_class(self):
        if self.request.method == "PATCH":
            return PswdChangeSerializer
        return UserSerializer

@api_view(["POST"])
# @permission_classes([~IsAuthenticated])
def user_login(request):
    user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
    if user is None:
        return Response({"error":_("Login yoki parol noto'g'ri!")}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    return Response({
                    "token":token.key,
                    "user":{
                        "id":user.id,
                        "username":user.username, 
                        "email":user.email, 
                        'phone':user.phone,
                        "first_name":user.first_name, 
                        "last_name":user.last_name
                        }
            }, status=status.HTTP_200_OK)


@api_view(['delete'])
@permission_classes([IsAuthenticated])
def user_logout(request):  #logout for both token & session
    if request.user.is_authenticated:
        if request.auth:
            request.auth.delete()
        else:
            logout(request)
        return Response({"ok":True, "data":_("Ko'rishguncha!")})
    return Response({"ok":False, "data":_("Siz avtorizatsiyadan o'tmagansiz!")})


