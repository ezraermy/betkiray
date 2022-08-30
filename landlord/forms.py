from django import forms

from .models import Akeray, AkerayImage

# Create your forms here 

class AkerayForm(forms.ModelForm):
    class Meta:
        model = Akeray
        fields = ('image', 'title', 'location', 'subcity', 'kebele', 'price', 'summary', 'phone')

class ImageForm(forms.ModelForm):
    image = forms.ImageField(
        label="image",
        widget=forms.ClearableFileInput(attrs={"multiple": True}),
    )
    class Meta:
        model = AkerayImage
        fields = ("image",)