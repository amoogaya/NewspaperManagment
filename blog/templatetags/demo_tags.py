from django import template
from blog.models import Advert

register = template.Library()


@register.inclusion_tag('blog/tags/adverts.html', takes_context=True)
def adverts(context):
    return {
        'adverts': Advert.objects.all(),
        'request': context['request'],
    }