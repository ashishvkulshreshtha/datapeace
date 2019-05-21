from django.urls import path

from .views import UserListApiView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserListApiView.as_view()),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view()),
]
