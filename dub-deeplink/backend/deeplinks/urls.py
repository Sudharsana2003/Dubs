from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /dl/
    path('watch/<int:video_id>/', views.watch_deeplink, name='watch'),  # /dl/watch/101/
]
