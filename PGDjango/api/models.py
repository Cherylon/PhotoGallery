from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(uniqe=True, max_length=255)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField()

     @models.permalink
    def get_absolute_url(self):
        return ('post_detail', (),
                {
                   'slug': self.slug,
                })

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['created_on']

        def __unicode__(self):
            return self.title




