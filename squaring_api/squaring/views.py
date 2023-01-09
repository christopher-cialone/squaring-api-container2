from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

# Create your views here.

class SquaringView(View):
    '''
    API that takes in a number and squares it mathematically through a 
    class based view
    the get request 'get's hit and the class below runs its program!
    '''
    def get(self, request, number):
        return HttpResponse(int(number) ** 2)


class HelloWorldView(View):
    '''
    This will take us to the home html page
    Views are the logic behind our entire app
    '''
    def get(self, request):
        return HttpResponse('Carmine and Christohper say Hello World')