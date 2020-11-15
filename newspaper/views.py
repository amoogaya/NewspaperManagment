from datetime import datetime
from . import forms
from django import forms as dj_form
from django.views import generic
from .models import Authors, MyUser
from django.forms import formset_factory, BaseFormSet
from newspaper.forms import ArticlesForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


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


class BaseArticleFormSet(BaseFormSet):
    def add_fields(self, form, index):
        super().add_fields(form, index)
        form.fields["my_field"] = dj_form.CharField()


def test_form_set(request):
    ArticleFormSet = formset_factory(ArticlesForm, formset=BaseArticleFormSet,
                                     extra=6, max_num=4, validate_max=True,
                                     can_order=True, can_delete=True)
    data = {
        'article-TOTAL_FORMS': '7',
        'article-INITIAL_FORMS': '0',
        'article-MAX_NUM_FORMS': '9',
        'article-0-title': 'Test',
        'article-0-category': 'sport',
        'article-0-author':  Authors.objects.get(username='Aya'),
        'article-0-body': 'test 1',
        'article-0-ORDER': '2',
        'article-0-my_field': 'hi',
        'article-1-title': 'Test',
        'article-1-category': 'sport',
        'article-1-author': Authors.objects.get(id=request.user.id),
        'article-1-user': 'sport',
        'article-1-body': 'test 2',
        'article-1-ORDER': '0',
        'article-1-my_field': 'hi',
        'article-2-title': 'aaa',
        'article-2-category': 'sport',
        'article-2-author': Authors.objects.get(username='Aya'),
        'article-2-pub_date': datetime.now(),
        'article-2-ORDER': '1',
        'article-2-DELETE': 'on',
        'article-2-my_field': 'hi',
    }
    if request.method == 'POST':
        formset = ArticleFormSet(request.POST, request.FILES, prefix='article')
        if formset.is_valid():
            pass
    else:
        formset = ArticleFormSet(data, prefix='article', initial=[
            {
                'title': 'Hi',
                'category': 'sport',
                'author': Authors.objects.get(username='fofe'),
                'body': 'test initial 1',
                'ORDER': '2',
            },
            {
                'title': 'Hi',
                'category': 'sport',
                'author': Authors.objects.get(username='fofe'),
                'body': 'test initial 2',
                'ORDER': '1',
            },
        ])
        print(formset.is_valid())
        print(formset.initial_form_count())
    return render(request, 'newspaper/forms_set_test.html', {'formset': formset})
