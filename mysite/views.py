from django.http import HttpResponse


def hello(request):
 text = "Hello World"
 return HttpResponse(text)

def blog(request):
 return HttpResponse("Blog Web Page modification")

def about_us(request):
 return HttpResponse("About US Web Page")

def my_func(req):
 return HttpResponse("About US Web Page")
