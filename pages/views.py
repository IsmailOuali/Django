from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'pages/index.html',{'name':'ismail', 'age':'23'})
