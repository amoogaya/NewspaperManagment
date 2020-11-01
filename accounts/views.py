from newspaper.forms import UserForm
from newspaper.models import Authors, OurUser
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            resigt_as = request.POST.get('resigt_as')
            password = request.POST.get('password')

            if resigt_as == 'Author':
                user = Authors.objects.create_user(first_name=first_name,
                                                   last_name=last_name,
                                                   username=username,
                                                   password=password,
                                                   resigt_as=resigt_as)
            else:
                user = OurUser.objects.create_user(first_name=first_name,
                                                   last_name=last_name,
                                                   username=username,
                                                   resigt_as=resigt_as)
            login(request, user)

            return redirect('newspaper:index')

    else:
        form = UserForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(request.POST)  # print it to verify if it take the information in right form

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('newspaper:index')
        else:
            print(form.error_messages)

    else:
        form = AuthenticationForm()
    return render(request, 'accounts/Login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('newspaper:index')
