"""Forms of the project."""
from django import forms
from .models import Thing

# Create your forms here.
class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {
            'description': forms.Textarea(),
            'quantity': forms.NumberInput()
            }

    def save(self):
        super().save(commit=False)
        return Thing.objects.create(
            name=self.cleaned_data.get('name'),
            description=self.cleaned_data.get('description'),
            quantity=self.cleaned_data.get('quantity')
        )