from django.shortcuts import render, HttpResponse, redirect
from security.forms import SignupForm
from django.contrib.auth import login, authenticate
from django.http import request
from django.urls import reverse



def registerUser(request):

    if request.method == 'POST':
        # When the request is POST, form is built-in Signup form populated with user data
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            # form is saved as cleaned_data dictionary
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request, user)
            return redirect('dashboard')

# When the request is 'Get', the form is blank built-in SignupForm
    form = SignupForm()
    return render(request, 'registeruser.html', {'form' : form})


