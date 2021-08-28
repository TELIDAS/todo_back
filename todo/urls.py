from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from todo import views

router = routers.DefaultRouter()
router.register('', views.ToDoView, basename='todo')
router2 = routers.DefaultRouter()
router2.register('', views.ToDoTextView, basename='todo_text')
urlpatterns = [
    path('api/todos/', include(router.urls)),
    path('api/todos/<int:id>/', include(router.urls)),
    path('api/v2/todos/', include(router2.urls)),
    path('api/v2/todos/<int:id>/', include(router2.urls)),
    path('api/register/', views.RegisterAPIView.as_view(), name='register-generic'),
    path('api/login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('api/token-verify/', TokenVerifyView.as_view(), name='token-verify'),
]