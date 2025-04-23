from django.urls import path

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


from .views import *
from django.contrib import admin
from django.urls import path, include

router = DefaultRouter()
router.register(r'users', RegisterViewSet, basename='user')
router.register(r"login-users", LoginViewSet, basename="login_viewset")

urlpatterns = [
    path('', include(router.urls)),
    path('RegisterApiView/', RegisterApiView.as_view(), name="RegisterApiView"),
    path('RegisterGenericsAPIView/', RegisterGenericsAPIView.as_view(), name='RegisterGenericsAPIView'),
    path('RegisterCreateApiView/', RegisterCreateApiView.as_view(), name="RegisterCreateApiView"),

    path("LoginApiview/", LoginApiview.as_view(), name="login_api_view"),
    path("LoginGenericView/", LoginGenericView.as_view(), name="login_generic"),
    path("login-fbv/", login_fbv, name="login_fbv"),


    path('logout/', LogoutAPIView.as_view(), name='logout'),





    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
