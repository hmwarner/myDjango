from django.contrib.syndication.views import Feed
from django.urls import reverse
from .models import Post

class LatestEntriesFeed(Feed):
    title = "My site news"
    link = "/feed/"
    description = "News developments at my site."

    def items(self):
        return Post.objects.order_by('-date_posted')[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content

    # item_link is only needed if Post has no get_absolute_url method.
    def item_link(self, item):
        return reverse('post-detail', args=[item.pk])
