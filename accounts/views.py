from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def register_view(request):
    """
    View for users to register a new account.
    Checks if form is valid, and responds accordingly,
    then redirects users to the login page on successfully
    creating a new account.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        "form": form,
    }
    return render(request, 'register.html', context)

@login_required
def profile_view(request):
    """
    Renders profile page for user with a form to update
    their information, already filled out with their current
    data.
    """

    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account info has been updated.')
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)

    context = {
        'form': form,
    }

    return render(request, 'profile.html', context)
