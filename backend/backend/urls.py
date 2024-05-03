
from django.contrib import admin
from django.urls import path,include
from api.views import UserView
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/register/',UserView.as_view(),name='user_register'),
    path('api/token/',TokenObtainPairView.as_view(),name='api_token'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='api_token_refresh'),
    path('api-auth/',include('rest_framework.urls')),
    path('api/',include('api.urls')),

]
