from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from wagtail.snippets.models import register_snippet


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname='full'),
    ]

    subpage_types = ['blog.BlogPage', ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(self, request, *args, **kwargs)

        context['blog_entries'] = BlogPage.objects.child_of(self).live()
        return context

    class Meta:
        verbose_name = "blogindexpage"
        verbose_name_plural = "blogindexpages"


class BlogPage(Page, index.Indexed):
    advert = models.ForeignKey(
        'blog.Advert',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
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
        InlinePanel('related_links', label='Related Links'),
        SnippetChooserPanel('advert'),

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


class BlogPageRelatedLink(Orderable):
    blog_page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='related_links')
    name = models.CharField(max_length=200)
    url = models.URLField()

    panels = [
        FieldPanel('name'),
        FieldPanel('url'),
    ]


@register_snippet
class Advert(models.Model):
    text = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
    ]

    def __str__(self):
        return self.text


class BlogPageAdvertPlacement(Orderable, models.Model):
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='+')
