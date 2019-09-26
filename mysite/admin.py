from django.contrib import admin
from mysite.models import Slideshow, Publisher, Book, Author


class SlideshowAdmin(admin.ModelAdmin):
    fields = ('Slideshow_img_url', 'Slideshow_url', 'Slideshow_title')


admin.site.register(Slideshow, SlideshowAdmin)
admin.site.register([Publisher, Book, Author])