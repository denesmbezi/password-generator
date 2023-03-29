from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'generator/home.html')

def password(request):
    if request.method == 'POST':
        characters = []

        if request.POST.get('uppercase'):
            characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

        if request.POST.get('lowercase'):
            characters.extend(list('abcdefghijklmnopqrstuvwxyz'))

        if request.POST.get('special'):
            characters.extend(list('!@#$%^/~&*()_+?":;|'))

        if request.POST.get('numbers'):
            characters.extend(list('0123456789'))

        if not characters:
            error_message = 'ERROR: Select an option to generate password'
            return render(request, 'generator/error.html', {'error_message': error_message})

        length = int(request.POST.get('length', 14))

        thepassword = ''
        for x in range(length):
            thepassword += random.choice(characters)

        return render(request, 'generator/password.html', {'password': thepassword})
    else:
        return render(request, 'generator/home.html')


def about(request):
    return render(request,'generator/about.html')
