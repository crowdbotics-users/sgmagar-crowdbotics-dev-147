
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.viewsets import ModelViewSet, ViewSet

from home.api.v1.serializers import SignupSerializer


class SignupViewSet(ModelViewSet):
    serializer_class = SignupSerializer
    http_method_names = ['post']


class LoginViewSet(ViewSet):
    serializer_class = AuthTokenSerializer

    def create(self, request):
        return ObtainAuthToken().post(request)
