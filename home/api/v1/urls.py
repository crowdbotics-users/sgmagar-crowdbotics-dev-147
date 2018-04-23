
from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from home.api.v1.viewsets import SignupViewSet, LoginViewSet

router = DefaultRouter()
router.register('signup', SignupViewSet, base_name='signup')
router.register('login', LoginViewSet, base_name='login')

urlpatterns = [
    url(r'', include(router.urls)),
]
