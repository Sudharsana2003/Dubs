from django.shortcuts import redirect
from django.http import HttpResponse

def watch_deeplink(request, video_id):
    """
    Simulates a deep link redirect.
    """
    target_url = f"https://example.com/watch/{video_id}"
    return redirect(target_url)

def index(request):
    return HttpResponse("Welcome to the Deeplinks section!")
