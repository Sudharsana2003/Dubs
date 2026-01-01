from django.urls import path
from .views import watch_deeplink

urlpatterns = [
    path("watch/<int:video_id>/", watch_deeplink),
]
