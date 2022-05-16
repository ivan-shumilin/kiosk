from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

def index(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'front/index.html', {'form': form})
    else:
        form = NameForm()
    return render(request, 'front/index.html', {'form': form})