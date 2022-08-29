
from django.urls import path
from django.http import HttpResponse


def test_func(request):
    return HttpResponse("Yu hooo!!")


urlpatterns = [
    path("test/", test_func),
]
