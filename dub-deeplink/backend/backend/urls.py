from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Dub Deeplink Backend!")

urlpatterns = [
    path('', home),            # /
    path('admin/', admin.site.urls),   # /admin/
    path('dl/', include('deeplinks.urls')),  # /dl/ and /dl/watch/<id>/
]
