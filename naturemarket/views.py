from django.shortcuts import render

def index_view(request):
    return render (request, 'index.html')

def teste_template(request):
    return render(request, "403.html")
