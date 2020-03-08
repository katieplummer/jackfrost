from django.db import models
import time

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    @property
    def images(self):
        return ArticleImage.objects.filter(article=self)

    @property
    def first_image(self):
        return self.images.first()
    
    @property
    def preview(self):
        return self.body[0:250]

    @property
    def timestamp(self):
        return self.date.strftime("%B") + ' ' + self.date.strftime("%d") + ", " + self.date.strftime("%Y")

    class Meta:
        ordering = ['-date']

class ArticleImage(models.Model):
    caption = models.TextField(default=None, null=True, blank=True)
    image = models.ImageField(upload_to="blog_images/")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)

# get last 3 articles for blog preview on home page

def blog_preview():
    return Article.objects.all()[:3]