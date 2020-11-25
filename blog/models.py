from django.db import models
from django.http import JsonResponse
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

    subpage_types = ['blog.BlogPage',]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(self, request, *args, **kwargs)

        context['blog_entries'] = BlogPage.objects.child_of(self).live()
        return context


class BlogPage(Page):
    body = RichTextField()
    date = models.DateField(" Post date ")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='related_links',
    )

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        FieldPanel('body', classname="full"),
        InlinePanel('related_links'),

    ]

    search_fields = Page.search_fields + [
        index.SearchField('body'),
        index.FilterField('date')
    ]

    promote_panels = [
        MultiFieldPanel(Page.promote_panels, "Common page configuration"),
        ImageChooserPanel('feed_image'),
    ]

    parent_page_types = ['blog.BlogIndexPage', ]
    subpage_types = []

    def serve(self, request):
        return JsonResponse({
            'title': self.title,
            'body': self.body,
            'date': self.date,
            'feed_image': self.feed_image.get_rendition('width-30').url,
        })


class BlogPageRelatedLink(Orderable):
    blog_page = models.ForeignKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=200)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]
