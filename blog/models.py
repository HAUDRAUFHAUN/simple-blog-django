from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Article(models.Model):
    """Model definition for Article."""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article")
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', default='images/default.png')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Article."""

        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self):
        """Unicode representation of Article."""
        pass
