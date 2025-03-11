from wagtail.models import Site
from blog.models import BlogIndexPage, TagsIndexPage

def navigation_pages(request):
    site = Site.find_for_request(request)
    homepage = site.root_page
    
    try:
        blogindex = BlogIndexPage.objects.live().first()
    except BlogIndexPage.DoesNotExist:
        blogindex = None
        
    try:
        tagsindex = TagsIndexPage.objects.live().first()
    except TagsIndexPage.DoesNotExist:
        tagsindex = None
    
    return {
        'navigation_homepage': homepage,
        'navigation_blogindex': blogindex,
        'navigation_tagsindex': tagsindex,
    }
