from newspaper.forms import UserForm
from newspaper.models import Author, OurUser
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Permission


# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            register_as = form.cleaned_data['register_as']
            password = form.cleaned_data['password1']

            if register_as == 'Author':
                user = Author.objects.create_user(first_name=first_name,
                                                  last_name=last_name,
                                                  username=username,
                                                  password=password,
                                                  register_as=register_as,
                                                  is_staff=True)
            else:
                user = OurUser.objects.create_user(first_name=first_name,
                                                   last_name=last_name,
                                                   username=username,
                                                   password=password,
                                                   register_as=register_as,
                                                   is_staff=False)

            user.set_password(form.cleaned_data["password1"])

            permission1 = Permission.objects.get(name='Can add article', )
            permission2 = Permission.objects.get(name='Can view article', )
            permission3 = Permission.objects.get(name='Can change article', )
            permission4 = Permission.objects.get(name='Can delete article', )
            user.user_permissions.add(permission1, permission2, permission3, permission4)

            permission11 = Permission.objects.get(name='Can add article images', )
            permission22 = Permission.objects.get(name='Can view article images', )
            permission33 = Permission.objects.get(name='Can change article images', )
            permission44 = Permission.objects.get(name='Can delete article images', )
            user.user_permissions.add(permission11, permission22, permission33, permission44)

            user.save()
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
    logout(request)
    return redirect('newspaper:index')
