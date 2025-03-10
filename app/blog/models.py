from django.db import models

# Add these:
from wagtail.models import Page
from wagtail.fields import RichTextField


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    max_count = 1

    content_panels = Page.content_panels + ["intro"]

    parent_page_types = ["home.HomePage"]
