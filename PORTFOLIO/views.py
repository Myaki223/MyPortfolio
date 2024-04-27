from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Category, GraphicDesign
from .forms import UIUXUpdateForm
from .forms import ImageForm


def home(request):
    categories = Category.objects.prefetch_related('graphicdesign_set')

    if request.method == 'POST':
        email =request.POST['email']
        name = request.POST['email']
        message = request.POST['message']

        send_mail(name, message, email,[settings.EMAIL_HOST_USER], fail_silently=True)

    context = {
        'categories':categories,
    }
    return render(request, 'MyPortfolio/index.html', context)
@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_page = request.POST.get('next', '')  # Get the value of 'next' parameter
            if next_page:  # If 'next' parameter exists, redirect to it
                return redirect(next_page)
            else:  # Otherwise, redirect to a default page
                return redirect('PORTFOLIO:admin')  # Use URL name to redirect
        else:
            # Add a Bootstrap alert indicating wrong password
            messages.error(request, 'Wrong username or password. Please try again.')
            return redirect('PORTFOLIO:login')  # Redirect back to login page on failure
    return render(request, 'MyPortfolio/admin.html')
@login_required
def user_view(request):
    images = GraphicDesign.objects.all()
    categories = Category.objects.prefetch_related('graphicdesign_set')

    context = {
        'categories':categories,
        'images':images,
    }

    return render(request, 'MyPortfolio/admin.html', context)

@login_required
def add_project(request):
    if request.POST:
        form = ImageForm(request.POST, request.FILES)
        print(request.FILES)
        if form.is_valid():
            form.save()

    return render(request, 'MyPortfolio/addproject.html',context={'form' : ImageForm})

@login_required
def delete_project(request, id):
    project = GraphicDesign.objects.get(id=id)

    if request.method == "POST" and "confirm_delete" in request.POST:
        project.delete()
        return redirect('PORTFOLIO:user')

    return render(request, 'MyPortfolio/deleteproject.html', {'project': project})

@login_required
def update_project(request, id):
    image = GraphicDesign.objects.get(id=id)  # Fetch a single Uiux object based on id
    if request.method == "POST":
        form = UIUXUpdateForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            form.save()
            return redirect('PORTFOLIO:user')
    else:
        form = UIUXUpdateForm(instance=image)
    return render(request, 'MyPortfolio/updateproject.html', {'form': form, 'image': image})

@login_required
def custom_logout(request):
    logout(request)
    # Redirect to a desired page after logout
    return redirect('PORTFOLIO:home')  # Replace 'home' with the name of your desired URL pattern