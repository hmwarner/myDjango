from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, PasswordChangingForm
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.http import HttpResponseRedirect

"""
def custom_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('blog-home')
    else:
        return login(request)
"""

class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('password_success')

def password_success(request):
    return render(request, 'registration/password_success.html', {})

@never_cache
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        next = request.GET.get('next')
        form = LoginForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                username = request.POST.get('username')
                password = request.POST.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    if user.get_short_name():
                        name = request.user.get_short_name()
                    else:
                        name = user
                    messages.info(request, f'Login Successful. Welcome back %s' % name)
                    if next == None:
                        return HttpResponseRedirect('/')
                    else:
                        return HttpResponseRedirect(next)
                else:
                    messages.error(request, f'The username and password combination is incorrect')

        context = {
            'form':form,
            'next':next,
            'title':'Login'
            }
        return render(request, 'users/login.html', context)

def register(request):
        if request.method == 'POST':
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your account has been created! You are now able to login as {username}.')
                #return redirect('login')
                login(request, user)
                return redirect("profile")
        else:
            form = UserRegisterForm()
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
        return render(request, 'users/register.html', {'form': form,'title':'Register'})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,
                                instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'title': 'Profile'
    }

    return render(request, 'users/profile.html', context)


from django.contrib.auth.models import User, Group
from blog.views import Post
from rest_framework import viewsets, permissions
from .permissions import IsOwnerOrReadOnly
from users.serializers import UserSerializer, GroupSerializer, PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    #API endpoint that allows users to be viewed or edited.

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    #API endpoint that allows groups to be viewed or edited.

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PostViewSet(viewsets.ModelViewSet):
    #API endpoint that allows posts to be viewed or edited.

    queryset = Post.objects.all()
    serializer_class = PostSerializer
