from django.shortcuts import render
def index(request):
    """ main page """
    context = {}
    template = 'index.html'
    return render(request, template, context)