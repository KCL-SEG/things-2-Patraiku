from django.shortcuts import render
from .forms import ThingForm

def home(request):
    if request.method == 'POST':
        form = ThingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home.html', {'form': ThingForm()})
        else:
            return render(request, 'home.html', {'form': form})
    return render(request, 'home.html', {'form': ThingForm()})
