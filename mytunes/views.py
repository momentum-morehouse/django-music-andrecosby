from django.shortcuts import render

def list_album(request):
    albums = Album.objects.all()
    return render(request, "albums/list_albums.html",
                  {"albums": albums})

def edit_album(request):
    albums = Album.objects.all()
    return render(request, "albums/edit_albums.html",
                  {"albums": albums})

def view_album(request):
    albums = Album.objects.all()
    return render(request, "albums/view_albums.html",
                  {"albums": albums})

def add_album(request):
    albums = Album.objects.all()
    return render(request, "albums/add_albums.html",
                  {"albums": albums})

# Create your views here.
