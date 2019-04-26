from django import forms
from hangman_app.models import Player


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = ("username",)
