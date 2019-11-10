from django import template

register = template.Library()

@register.filter(name='build_search_url')
def build_search_url(absolute_url):
    """
    Custom tag for pagination to filter
    out the previous page from absolute url
    """
    if '&page=' in absolute_url:
        absolute_url = absolute_url.split('&page=')[0]
    return absolute_url
