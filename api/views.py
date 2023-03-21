from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse("<h2> This is a test for Code Freak's app </h2>")
