from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import MiniUrlForm, UserForm, SigninForm
from .models import MiniUrl


# Create your views here.
@login_required
def home(request):
    mini_urls = MiniUrl.objects.all()
    return render(request, 'mini_url/home.html', {'minis': mini_urls})


@login_required
def create_url(request):
    if request.method == 'POST':
        form = MiniUrlForm(request.POST)
        if form.is_valid():
            mini = form.save(commit=False)
            mini.author = request.user
            form.save()
            return redirect('home')
        else:
            return render(request, 'mini_url/create_url.html', {'form': form})
    else:
        form = MiniUrlForm()
        return render(request, 'mini_url/create_url.html', {'form': form})


@login_required
def access(request, code):
    mini_url = get_object_or_404(MiniUrl, code=code)
    mini_url.nb_access += 1
    mini_url.save()

    return redirect(mini_url.url, permanent=True)


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request, 'mini_url/register.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'mini_url/register.html', {'form': form})


def signin(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            if user:
                login(request, user)
            return redirect('home')
        else:
            return render(request, 'mini_url/signin.html', {'form': form})
    else:
        form = SigninForm()
        return render(request, 'mini_url/signin.html', {'form': form})

