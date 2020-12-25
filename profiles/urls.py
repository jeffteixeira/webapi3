from django.urls import path
from profiles import views


urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name=views.ProfileList.name),
    path('profiles/<int:pk>', views.ProfileDetail.as_view(), name=views.ProfileDetail.name),
    path('profile-posts/', views.ProfilePostsList.as_view(), name=views.ProfilePostsList.name),
    path('profile-posts/<int:pk>', views.ProfilePostsDetail.as_view(), name=views.ProfilePostsDetail.name)
]
