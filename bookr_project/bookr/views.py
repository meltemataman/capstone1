
# Create your views here.
from django.http import HttpResponse

def welcome_view(request):
    return HttpResponse("<h1>Welcome to Bookr!</h1>")