from django.forms import ModelForm
from .models import PointEau


class PointEauForm(ModelForm):
    class Meta:
        model = PointEau
        fields = ['nom', 'lat', 'long', 'desc']

    # def save(self, commit=True):
    #     pointEau = super(ModelForm, self).save(commit=False)
    #     pointEau.nom = self.cleaned_data['nom']
    #     pointEau.lat = self.cleaned_data['lat']
    #     pointEau.long = self.cleaned_data['long']
    #     pointEau.desc = self.cleaned_data['desc']
    #     if commit:
    #         pointEau.save()

    #     return pointEau


class EditPointEauForm(ModelForm):
    class Meta:
        model = PointEau
        exclude = ['owner']
