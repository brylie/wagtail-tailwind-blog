from wagtail.models import Site
from blog.models import BlogIndexPage

def navigation_pages(request):
    site = Site.find_for_request(request)
    homepage = site.root_page
    try:
        blogindex = BlogIndexPage.objects.live().first()
    except BlogIndexPage.DoesNotExist:
        blogindex = None
    
    return {
        'navigation_homepage': homepage,
        'navigation_blogindex': blogindex,
    }
