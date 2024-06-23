from django.contrib.auth.forms import UserCreationForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email", )


class SearchIdForm(forms.Form):
    search_id = forms.IntegerField(label='ID de la nave: ',)
