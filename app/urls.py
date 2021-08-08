from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from authapp.views import UserApiView
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('users', UserApiView)

urlpatterns = [
   path('admin/', admin.site.urls),
   path('api-token-auth/', views.obtain_auth_token),
   path('api/v1/', include(router.urls)),
]
