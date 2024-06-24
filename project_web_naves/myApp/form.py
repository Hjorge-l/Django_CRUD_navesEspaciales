from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class SearchIdForm(forms.Form):
    search_id = forms.IntegerField(label='ID de la nave: ',)


class SearchNameForm(forms.Form):
    search_name = forms.CharField(label='Nombre del la nave: ',  max_length=20)
