from django.urls import path
from . import views
from .views import PostCreateView, PostUpdateView, PostDeleteView, homepages1

urlpatterns = [
    path('', views.homepages1, name='homepages1'),
    path('blog', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('detail/<int:post_id>/', views.post_detail, name='detail'),
    path('new_post/', PostCreateView.as_view(), name='new_post'),
    path('detail/<slug:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('detail/<slug:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
