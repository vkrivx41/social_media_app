from django.shortcuts import render, redirect, HttpResponse


def home(request) -> HttpResponse:
    # redirect from / to posts/
    if request.get_full_path() == "/":
        return redirect(to="app_contents:home")

    return HttpResponse("<h1>Home</h1>")

def create(request) -> HttpResponse:
    return HttpResponse("<h1>Create a Post</h1>")

def delete(request, id: int) -> HttpResponse:
    return HttpResponse("<h1>Delete</h1>")

def update(request, id: int) -> HttpResponse:
    return HttpResponse("<h1>Update</h1>")
