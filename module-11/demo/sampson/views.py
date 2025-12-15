from django.http import HttpResponse

def home(request):
    return HttpResponse("Drew says Hello!")
