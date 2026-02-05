from django import forms
from . import models


class AddLaptopForm(forms.ModelForm):
    class Meta:
        model = models.Laptop
        fields = '__all__'

class AddDesktopForm(forms.ModelForm):
    class Meta:
        model = models.Desktop
        fields = '__all__'

class AddMobileForm(forms.ModelForm):
    class Meta:
        model = models.Mobile
        fields = '__all__'