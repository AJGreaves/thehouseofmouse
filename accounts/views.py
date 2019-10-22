from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}! You can now log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)
    
def profile_view(request):
    return render(request, 'profile.html')
    