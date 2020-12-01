from django.shortcuts import render

from wagtail.search.utils import parse_query_string
from wagtail.search.models import Query
from wagtail.core.models import Page


# Create your views here.
def search(request):
    search_query = request.GET.get('query', None)
    if search_query:
        search_results = Page.objects.live().search(search_query)
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    return render(request, 'blog/search_results.html', {
        'search_query': search_query,
        'search_results': search_results
    })
