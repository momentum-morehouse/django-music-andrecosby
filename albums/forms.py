from django import forms
from .models import Album, Artist

class AlbumForm(forms.Form):
            title = forms.CharField(max_length=300)
            artist = forms.CharField(max_length=300)
            year_released = forms.DateField()
            image_url = forms.URLField
        


class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = [
            'name',
            'bio',
        ]