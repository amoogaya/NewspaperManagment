from django.shortcuts import render, redirect
from .models import Authors, MyUser
from django.contrib.auth.decorators import login_required
from . import forms
from django.views import generic


# Create your views here.

class IndexView(generic.ListView):
    model = Authors
    template_name = 'newspaper/index.html'
    context_object_name = 'authors'


class AuthorsDetailedView(generic.DetailView):
    model = Authors
    template_name = 'newspaper/detail.html'


@login_required(login_url='/accounts/login', redirect_field_name='/newspaper/createArticle.html')
def article_add(request):
    print(True)
    
    username = request.user.username
    print(username)
    the_user = MyUser.objects.get(username=username)

    if the_user.register_as == 'Author':
        if request.method == 'POST':
            form = forms.ArticlesForm(request.POST)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                return redirect("newspaper:index")
        else:
            form = forms.ArticlesForm()
            return render(request, 'newspaper/createArticle.html', {'form': form})

    else:
        return redirect("newspaper:index")
