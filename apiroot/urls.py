from django.urls import path
from .views import ApiRoot


urlpatterns = [
    path('', ApiRoot.as_view(), name='api-root')
]
