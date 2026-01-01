from django.shortcuts import redirect
from django.http import HttpResponse

def watch_deeplink(request, video_id):
    """
    Simulates a deep link redirect.
    In real usage, this would open the mobile app or fallback to web.
    """
    target_url = f"https://example.com/watch/{video_id}"
    return redirect(target_url)
