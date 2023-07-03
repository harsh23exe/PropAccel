from django.urls import path
from django.views.decorators.http import require_http_methods

from .views import UserDetailView, UserCreateView, UserUpdateView

urlpatterns = [
    path('', require_http_methods(['POST'])(UserCreateView.as_view()), name='user_create'),
    path('<int:pk>/', require_http_methods(['GET'])(UserDetailView.as_view()), name='user_detail'),
    path('<int:pk>/', require_http_methods([ 'PATCH'])(UserUpdateView.as_view()), name='user_update'),
]
