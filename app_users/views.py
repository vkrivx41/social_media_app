from django.shortcuts import render, HttpResponse


def signin(request) -> HttpResponse:
    return HttpResponse("<h1>Signin</h1>")

def signup(request) -> HttpResponse:
    return HttpResponse("<h1>Signup</h1>")

def signout(request) -> HttpResponse:
    return HttpResponse("<h1>Signout</h1>")

def profile(request, username: str) -> HttpResponse:
    return HttpResponse("<h1>Profile</h1>")

def delete(request, username: str) -> HttpResponse:
    return HttpResponse("<h1>Delete</h1>")

def update(request, username: str) -> HttpResponse:
    return HttpResponse("<h1>Update</h1>")
