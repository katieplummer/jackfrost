from django.db import models

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

class ArticleImage(models.Model):
    caption = models.TextField(default=None, null=True, blank=True)
    image = models.ImageField(upload_to="blog_images/")
    article = models.ForeignKey(Article, on_delete=models.CASCADE, default=None)

