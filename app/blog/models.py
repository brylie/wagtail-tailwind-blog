from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    max_count = 1

    content_panels = Page.content_panels + ["intro"]

    parent_page_types = ["home.HomePage"]


class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + ["date", "intro", "body"]

    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []