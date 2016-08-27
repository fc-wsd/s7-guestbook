from django.shortcuts import render
from django.http import HttpResponse


def toppage(request):
    text = 'hello world'
    response = HttpResponse(text)
    return response

