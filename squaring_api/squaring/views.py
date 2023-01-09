from django.shortcuts import render
from django.http import HttpResponse
from django.views import View 

# Create your views here.

class SquaringView(View):
    '''
    API that takes in a number and squares it mathematically through a 
    class based view the get request 'get's hit and the class below runs its program
    '''
    def get(self, request, number):
        return HttpResponse(number ** 2)


# class HelloWorldView(View):
#     def get(self, request):
#         return HttpResponse('Hello world!')