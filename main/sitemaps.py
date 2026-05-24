from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'monthly'

    def items(self):
        return ['index', 'menu', 'gallery', 'contact', 'reservation', 'cafe', 'organizations']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        if item == 'index':
            return 1.0
        elif item in ['menu', 'reservation']:
            return 0.8
        else:
            return 0.5
