from django.urls import path,include
from passapp.views import RegisterView,ChangePasswordAPI 
from rest_framework import routers
from passapp import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name='passapp'
router=routers.DefaultRouter()
router.register('rest',RegisterView, basename='rest')

urlpatterns = [
    path('', include(router.urls)),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/change_password/',ChangePasswordAPI.as_view(),name='change_password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


]