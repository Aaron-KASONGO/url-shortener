from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.utils.decorators import method_decorator
from django.views import generic
from .forms import MiniUrlForm, UserForm, SigninForm
from .models import MiniUrl
from django.contrib import messages


"""@login_required
def home(request):
    mini_urls = MiniUrl.objects.all()
    return render(request, 'mini_url/home.html', {'minis': mini_urls})"""

# Class based view which do the same with the home function
@method_decorator(login_required, name='dispatch')
class HomeView(generic.ListView):
    model = MiniUrl
    context_object_name = 'minis'
    template_name = 'mini_url/home.html'
    
    def get_queryset(self):
        return MiniUrl.objects.filter(author=self.request.user)


"""@login_required
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
        return render(request, 'mini_url/create_url.html', {'form': form})"""

@method_decorator(login_required, name='dispatch')
class CreateUrlView(generic.CreateView):
    model = MiniUrl
    template_name = 'mini_url/create_url.html'
    form_class = MiniUrlForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        mini = form.save(commit=False)
        mini.author = self.request.user
        form.save()
        return redirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class UpdateUrlView(generic.UpdateView):
    model = MiniUrl
    template_name = 'mini_url/create_url.html'
    form_class = MiniUrlForm
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniUrl, code=code)


@method_decorator(login_required, name='dispatch')
class DeleteUrlView(generic.DeleteView):
    model = MiniUrl
    context_object_name = 'mini_url'
    template_name = 'mini_url/delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        code = self.kwargs.get('code', None)
        return get_object_or_404(MiniUrl, code=code)


@login_required
def access(request, code):
    mini_url = get_object_or_404(MiniUrl, code=code)
    mini_url.nb_access += 1
    mini_url.save()

    return redirect(mini_url.url, permanent=True)


def register(request):
    messages.info(request, "Enregistrez-vous")
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, f"Bien venue {request.user.username}")
            return redirect('shortener')
        else:
            return render(request, 'mini_url/register.html', {'form': form})
    else:
        form = UserForm()
        return render(request, 'mini_url/register.html', {'form': form})


"""def signin(request):
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
        return render(request, 'mini_url/signin.html', {'form': form})"""

class Login(views.LoginView):
    template_name = 'mini_url/page.html'

class Logout(views.LogoutView):
    next_page = reverse_lazy('home')

class ChangePasswordView(views.PasswordChangeView):
    template_name = 'mini_url/passwordchange.html'
    success_url = reverse_lazy('home')

class PasswordDone(views.PasswordChangeDoneView):
    tempalte_name = 'mini_url/passwordchange_done.html'