from django.urls import path
from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view(), name=views.PostList.name),
    path('posts/<int:pk>', views.PostDetail.as_view(), name=views.PostDetail.name),
    path('posts-comments/', views.PostCommentList.as_view(), name=views.PostCommentList.name),
    path('posts-comments/<int:pk>', views.PostCommentDetail.as_view(), name=views.PostCommentDetail.name)
]
