from django.db import models

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.search import index
from wagtail.admin.panels import FieldPanel
from django.db.models import Count
from django.shortcuts import render


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    max_count = 1

    content_panels = Page.content_panels + ["intro"]

    parent_page_types = ["home.HomePage"]

    def get_context(self, request):
        context = super().get_context(request)
        blogpages = BlogPage.objects.live().order_by("-date")
        context['blogpages'] = blogpages
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + ["date", "intro", "body", "tags"]

    parent_page_types = ["blog.BlogIndexPage"]
    subpage_types = []


class TagsIndexPage(Page):
    intro = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    
    max_count = 1

    parent_page_types = ["home.HomePage"]
    
    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        
        blog_pages = BlogPage.objects.live()

        tag = request.GET.get('tag')
        
        if tag:
            context['tag'] = tag
            context['blog_pages'] = blog_pages.filter(tags__name=tag)
            context['is_filtered'] = True
        else:
            # Otherwise get all tags with count for the tag cloud
            tags = blog_pages.values('tags__name').annotate(
                tag_count=Count('tags__name')
            ).exclude(tags__name=None).order_by('-tag_count')
            
            context['tags'] = tags
            context['is_filtered'] = False
            
        return context
    
    class Meta:
        verbose_name = "Tags Index Page"