from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView

from todo import views
from todo.views import TokenObtainPairViewEDITED

router = routers.DefaultRouter()
router.register('', views.ToDoTextView, basename='todo_text')
urlpatterns = [
    path('api/v2/todos/', include(router.urls)),
    path('api/v2/todos/<int:id>/', include(router.urls)),
    path('api/register/', views.RegisterAPIView.as_view(), name='register-generic'),
    path('api/login/', TokenObtainPairViewEDITED.as_view(), name='token-obtain-pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]
