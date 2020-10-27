from django.shortcuts import get_object_or_404, redirect, render

from albums.forms import AlbumForm

from .models import Album, Artist


def list_albums(request):
    album = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": Album})

def edit_albums(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'GET':
        form = AlbumForm(instance=album)
    return render(request, "albums/edit_albums.html",
                  {"album": Album})

def view_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    return render(request, "albums/view_albums.html",
                  {"albums": Album})

def add_album(request):
    if request.method == 'GET':
        form = AlbumForm()
    else:
        form = AlbumForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            title = data.get('title')
            artist = data.get('artist')
            year_released = data.get('year_released')
            image_url = data.get('image_url')
            form.save()
            return render(request, "albums/add_albums.html", {"form": form})

def delete_album(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == 'POST':
        Album.delete()
        return redirect(to='list_album')

    return render(request, "albums/delete_album.html",
                  {"album": Album})

# Create your views here.
