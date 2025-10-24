from django.shortcuts import render, HttpResponse

def about(request) -> HttpResponse:
    return HttpResponse("<h1>About Page</h1>")