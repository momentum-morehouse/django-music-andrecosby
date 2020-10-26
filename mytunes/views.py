from django.shortcuts import render, redirect, get_object_or_404
from .models import Album

def list_album(request):
    mytunes = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": mytunes})

def edit_album(request, pk):
    Album = get_object_or_404(all, pk=pk)
    if request.method == 'GET':
        form.save()
    return render(request, "albums/edit_albums.html",
                  {"albums": mytunes})

def view_album(request):
    mytunes = mytunes.objects.all()
    return render(request, "albums/view_albums.html",
                  {"albums": mytunes})

def add_album(request):
    mytunes = mytunes.objects.all()
    return render(request, "albums/add_albums.html",
                  {"albums": mytunes})

# Create your views here.
