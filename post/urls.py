from django.urls import path
from .views import PostListView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    
    # Post endpoints
    path('', PostCreateView.as_view(), name='post_create'),
    path('', PostListView.as_view(), name='post_list'),
    
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/', PostDeleteView.as_view(), name='post_delete'),
]
