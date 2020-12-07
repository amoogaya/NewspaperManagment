from django.db import models
from wagtail.core import blocks
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.core.fields import StreamField
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page, Orderable
from wagtail.images.blocks import ImageChooserBlock
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, StreamFieldPanel


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
        verbose_name = "blog index page"
        verbose_name_plural = "blog index pages"


class PersonBlock(blocks.StructBlock):
    first_name = blocks.CharBlock()
    surname = blocks.CharBlock()
    photo = ImageChooserBlock(required=False)
    biography = blocks.RichTextBlock()

    class Meta:
        template = 'blog/blocks/person.html'
        icon = 'user'


class BlogPage(Page, index.Indexed):
    brief_description = RichTextField()
    date = models.DateField(" Post date ")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='related_links',
    )

    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="full title",
                                     help_text='the title of related blog',
                                     group='Hi')),
        ('paragraph', blocks.RichTextBlock(group='Hi')),
        ('images', ImageChooserBlock()),
        ('domain', blocks.FloatBlock()),

    ], null=True, )

    additional_information = StreamField([
        ('date', blocks.DateTimeBlock()),

        ('blog_number', blocks.RegexBlock(regex='[0-9]{3}[a-d]',
                                          error_messages={
                                              'invalid': "the number of blog is not valid."})),

        ('category', blocks.ChoiceBlock(choices=[('history', 'History'),
                                                 ('tourism', 'Tourism'),
                                                 ('sport', 'Sport'),
                                                 ], icon='list')),

        ('author', PersonBlock()),

    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel('brief_description'),
        FieldPanel('date'),
        InlinePanel('related_links', label='Related Links'),
        InlinePanel('advert_placements', label='Adverts'),
        StreamFieldPanel('body'),
        StreamFieldPanel('additional_information'),
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
class Advert(index.Indexed, models.Model):
    text = models.CharField(max_length=200)
    url = models.URLField(null=True, blank=True)

    panels = [
        FieldPanel('text'),
        FieldPanel('url'),
    ]

    search_fields = [
        index.SearchField('text', partial_match=True)
    ]

    def __str__(self):
        return self.text


class BlogPageAdvertPlacement(Orderable, models.Model):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='advert_placements')
    advert = models.ForeignKey(Advert, on_delete=models.CASCADE, related_name='+')

    class Meta(Orderable.Meta):
        verbose_name = 'advert placement'
        verbose_name_plural = 'advert placements'

    panels = [
        SnippetChooserPanel('advert')
    ]

    def __str__(self):
        return self.page.title + " -> " + self.advert.text
