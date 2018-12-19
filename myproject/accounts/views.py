from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

# Create your views here.

def signup(request):
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

